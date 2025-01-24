from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import joblib
import logging
from transformers import TFAutoModelForCausalLM, AutoTokenizer
import tensorflow as tf
from .forms import BlogPostForm
from .models import BlogPost
from .models import Comment
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .responses import keyword_responses
import pandas as pd
import json
import os
import csv
from django.shortcuts import render

logger = logging.getLogger(__name__)

csv_path = os.path.abspath('career_counseling/data/dropout_data.csv')


# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load the trained model for dropout prediction
model = joblib.load('career_counseling/ml_model/trained_model.pkl')

# Initialize GPT-2 model and tokenizer for the chatbot (using TensorFlow)
tokenizer = AutoTokenizer.from_pretrained("gpt2")
chatbot_model = TFAutoModelForCausalLM.from_pretrained("gpt2")

# Mapping of numeric values back to descriptive text
DROPOUT_REASON_MAP = {
    1: "Financial difficulties",
    2: "Personal reasons (health, family obligations, etc.)",
    3: "Dissatisfaction with the curriculum",
    4: "Lack of interest in chosen field of study",
    5: "Other"
}

CHALLENGES_MAP = {
    1: "Academic pressure",
    2: "Financial constraints",
    3: "Personal issues",
    4: "Lack of interest in the subject",
    5: "Other"
}

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        logger.debug(f"Form POST data: {request.POST}")
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.debug(f"User {user} logged in successfully")
            return redirect('home')
        else:
            logger.debug(f"Form errors: {form.errors}")
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to homepage after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def create_blog_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Assign the logged-in user as the author
            blog_post.save()
            return redirect('blog')  # Redirect to the blog listing page
    else:
        form = BlogPostForm()
    return render(request, 'create_blog.html', {'form': form})


@login_required
def delete_blog_view(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        blog_post.delete()
        return HttpResponseRedirect(reverse('blog'))  # Redirect to blog page after deletion
    return render(request, 'delete_blog.html', {'blog_post': blog_post})

@login_required
def like_blog_view(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    if request.user in blog_post.likes.all():
        blog_post.likes.remove(request.user)
    else:
        blog_post.likes.add(request.user)
    return redirect('blog')


@login_required
def add_comment_view(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        text = request.POST.get('comment')
        if text:
            comment = Comment.objects.create(blog_post=blog_post, author=request.user, text=text)
            comment.save()
    return redirect('blog')





def logout_view(request):
    logout(request)
    return redirect('home')


def admin_dashboard_view(request):
    df = pd.read_csv('career_counseling/data/dropout_data.csv')

    # Existing data processing
    dropout_risk_data = df.groupby('dropout_risk')['risk_count'].sum().to_dict()
    monthly_dropout_data = df.groupby('month')['monthly_count'].sum().to_dict()
    dropout_reasons_data = df.groupby('reason')['reason_count'].sum().to_dict()
    gender_risk_data = df.groupby('gender')['gender_count'].sum().to_dict()
    support_needs_data = df.groupby('support_type')['support_count'].sum().to_dict()

    # New data processing
    age_group_data = df.groupby('age_group')['age_group_count'].sum().to_dict()
    study_hours_data = df.groupby('study_hours')['study_hours_count'].sum().to_dict()
    region_data = df.groupby('region')['region_count'].sum().to_dict()

    context = {
        'dropout_risk_data': json.dumps(dropout_risk_data),
        'monthly_dropout_data': json.dumps(monthly_dropout_data),
        'dropout_reasons_data': json.dumps(dropout_reasons_data),
        'gender_risk_data': json.dumps(gender_risk_data),
        'support_needs_data': json.dumps(support_needs_data),
        'age_group_data': json.dumps(age_group_data),
        'study_hours_data': json.dumps(study_hours_data),
        'region_data': json.dumps(region_data),
    }

    return render(request, 'admin_dashboard.html', context)



# View for the dropout analysis page
def dropout_analysis_view(request):
    if request.method == 'POST':
        # Extract user inputs from the form
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        education_level = request.POST['education_level']
        dropout_reason = int(request.POST['dropout_reason'])
        challenges = int(request.POST['challenges'])
        support_importance = int(request.POST['support_importance'])
        interests = request.POST['interests']
        career_aspirations = request.POST['career_aspirations']

        # Preprocess input for the model
        input_data = [[dropout_reason, challenges, support_importance]]
        prediction = model.predict(input_data)

        # Convert the numeric values back to descriptive text
        dropout_reason_text = DROPOUT_REASON_MAP[dropout_reason]
        challenges_text = CHALLENGES_MAP[challenges]

        prediction_message = (
            "You are at risk of dropping out. It might be helpful to seek further support and consider alternative learning strategies."
            if prediction == 1
            else "You are not at high risk of dropping out. Keep working towards your goals and seek support if needed."
        )

        file_path = os.path.abspath('career_counseling/data/dropout_details.csv')

        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Write headers only if the file is empty (check if it's the first time)
            if file.tell() == 0:
                writer.writerow([
                    "Name", "Age", "Gender", "Education Level", "Dropout Reason", "Challenges", 
                    "Support Importance", "Interests", "Career Aspirations"
                ])
            
            # Write the user data to the CSV file
            writer.writerow([
                name, age, gender, education_level, dropout_reason_text, challenges_text,
                support_importance, interests, career_aspirations
            ])

        # Render the prediction results
        return render(request, 'results.html', {
            'name': name,
            'age': age,
            'gender': gender,
            'education_level': education_level,
            'dropout_reason': dropout_reason_text,
            'challenges': challenges_text,
            'support_importance': support_importance,
            'interests': interests,
            'career_aspirations': career_aspirations,
            'prediction': prediction_message
        })

    return render(request, 'dropout_analysis.html')

def predict_dropouts(request):
    if request.method == 'POST':
        # Extract user inputs from the form
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        education_level = request.POST['education_level']
        dropout_reason = int(request.POST['dropout_reason'])
        challenges = int(request.POST['challenges'])
        support_importance = int(request.POST['support_importance'])
        interests = request.POST['interests']
        career_aspirations = request.POST['career_aspirations']

        # Preprocess input for the model
        input_data = [[dropout_reason, challenges, support_importance]]
        prediction = model.predict(input_data)

        # Convert the numeric values back to descriptive text
        dropout_reason_text = DROPOUT_REASON_MAP[dropout_reason]
        challenges_text = CHALLENGES_MAP[challenges]

        prediction_message = "You are at risk of dropping out. It might be helpful to seek further support and consider alternative learning strategies." if prediction == 1 else "You are not at high risk of dropping out. Keep working towards your goals and seek support if needed."

        # Render the prediction results
        return render(request, 'results.html', {
            'name': name,
            'age': age,
            'gender': gender,
            'education_level': education_level,
            'dropout_reason': dropout_reason_text,
            'challenges': challenges_text,
            'support_importance': support_importance,
            'interests': interests,
            'career_aspirations': career_aspirations,
            'prediction': prediction_message
        })
    return render(request, 'index.html')

def generate_response(prompt):
    # Tailor the prompt to provide better guidance to the model
    refined_prompt = f"You are a helpful and friendly chatbot that assists with career advice and general questions. Respond to the following user message in a helpful manner:\n\nUser: {prompt}\nChatbot:"
    
    input_ids = tokenizer.encode(refined_prompt + tokenizer.eos_token, return_tensors="tf")
    response_ids = chatbot_model.generate(input_ids, max_length=150, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    
    # Clean up the response to make it more conversational
    cleaned_response = response.replace(refined_prompt, "").strip()
    return cleaned_response

def chatbot_response(request):
    user_message = request.GET.get('message', '').lower()
    logging.debug(f"User message received: {user_message}")

    # Check if the message matches any predefined keywords
    for keyword, long_response in keyword_responses.items():
        if keyword in user_message:
            response = long_response
            break
    else:
        # Use AI-based model for less common or open-ended questions
        response = generate_response(user_message)

    logging.debug(f"Response sent: {response}")
    return JsonResponse({'response': response})

def chatbot_view(request):
    return render(request, 'chatbot.html')

# View for the homepage
def home(request):
    return render(request, 'home.html')

def blog_view(request):
    # Fetch all blog posts from the database
    blog_posts = BlogPost.objects.all().order_by('-created_at')  # Fetch in reverse chronological order
    return render(request, 'blog.html', {'blog_posts': blog_posts})


# View for chatbot page (optional, if separate page)
def chatbot_view(request):
    return render(request, 'chatbot.html')
