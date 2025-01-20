# from flask import Flask, render_template, request, jsonify
# import openai
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)

# # Configure Flask app
# app.secret_key = os.getenv('FLASK_SECRET_KEY')

# # Configure OpenAI
# openai.api_key = os.getenv('OPENAI_API_KEY')

# # Verify environment variables are loaded
# def verify_env():
#     required_vars = ['OPENAI_API_KEY', 'FLASK_SECRET_KEY']
#     missing_vars = [var for var in required_vars if not os.getenv(var)]
    
#     if missing_vars:
#         raise EnvironmentError(
#             f"Missing required environment variables: {', '.join(missing_vars)}\n"
#             "Please check your .env file and ensure all required variables are set."
#         )

# # System message to guide the AI's responses
# SYSTEM_MESSAGE = """You are a supportive mental health assistant for students. Your role is to:
# 1. Provide empathetic, non-judgmental responses
# 2. Help students find mental health resources in their area
# 3. Share coping strategies and self-help techniques
# 4. Direct users to emergency services when needed
# 5. Provide information about common mental health challenges students face
# 6. Offer resources related to medical help for injuries and mental depression."""

# @app.route('/')
# def home():
#     return render_template('index2.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json.get('message', '').strip()
    
#     if not user_message:
#         return jsonify({'error': 'No message provided.'}), 400
    
#     try:
#         # Call OpenAI API using the correct method
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": SYSTEM_MESSAGE},
#                 {"role": "user", "content": user_message}
#             ],
#             temperature=0.7,
#             max_tokens=500
#         )
        
#         ai_response = response.choices[0].message['content'].strip()
        
#         # Check for crisis keywords
#         crisis_keywords = [
#             'suicide', 'kill myself', 'want to die', 'end it all', 
#             'hurt myself', 'depression', 'self-harm', 'anxiety', 
#             'panic', 'overwhelmed'
#         ]
#         if any(keyword in user_message.lower() for keyword in crisis_keywords):
#             emergency_response = "\n\n🚨 **IMPORTANT:** If you're experiencing severe emotional distress, please reach out for immediate help:\n"
#             emergency_response += "• [National Suicide Prevention Lifeline (988)](tel:988)\n"
#             emergency_response += "• [Crisis Text Line: Text HOME to 741741](https://www.crisistextline.org/)\n"
#             emergency_response += "• [Emergency Services: 911](tel:911)\n"
#             emergency_response += "\nYou’re not alone, and help is available."
            
#             ai_response += emergency_response
        
#         return jsonify({'response': ai_response})
    
#     except openai.error.OpenAIError as e:
#         # Handle specific OpenAI errors
#         return jsonify({'error': f"OpenAI API error: {e}"}), 500
#     except Exception as e:
#         # Handle general errors
#         return jsonify({'error': str(e)}), 500

# @app.route('/resources')
# def resources():
#     # Define a list of resources related to mental health, medical help, injuries, and depression
#     resources_list = [
#         {
#             'category': 'Mental Health Support',
#             'resources': [
#                 {'name': 'National Alliance on Mental Illness (NAMI)', 'description': 'Education, support, and advocacy for individuals with mental illness.', 'link': 'https://www.nami.org/Home'},
#                 {'name': 'Depression and Bipolar Support Alliance (DBSA)', 'description': 'Support groups and resources for managing depression.', 'link': 'https://www.dbsalliance.org/'},
#                 {'name': 'Mental Health America (MHA)', 'description': 'Resources and information on mental health disorders.', 'link': 'https://www.mhanational.org/'},
#             ]
#         },
#         {
#             'category': 'Medical Help for Injuries',
#             'resources': [
#                 {'name': 'Local Emergency Services', 'description': 'Dial 911 for immediate medical assistance.', 'link': 'tel:911'},
#                 {'name': 'Urgent Care Centers', 'description': 'Find nearby urgent care for non-life-threatening injuries.', 'link': 'https://www.urgentcare.com/'},
#                 {'name': 'Poison Control', 'description': 'Immediate assistance for poison-related emergencies.', 'link': 'tel:800-222-1222'},
#             ]
#         },
#         {
#             'category': 'Depression Resources',
#             'resources': [
#                 {'name': 'SAMHSA National Helpline', 'description': '24/7, free and confidential treatment referral and information services.', 'link': 'tel:1-800-662-HELP (4357)'},
#                 {'name': 'National Suicide Prevention Lifeline', 'description': '24/7 free and confidential support for people in distress.', 'link': 'tel:988'},
#                 {'name': 'Crisis Text Line', 'description': 'Free text support available 24/7 by texting HOME to 741741.', 'link': 'https://www.crisistextline.org/'},
#             ]
#         },
#         {
#             'category': 'Substance Abuse Help',
#             'resources': [
#                 {'name': 'Alcoholics Anonymous (AA)', 'description': 'Support groups for individuals struggling with alcohol addiction.', 'link': 'https://www.aa.org/'},
#                 {'name': 'Narcotics Anonymous (NA)', 'description': 'Support groups for individuals struggling with drug addiction.', 'link': 'https://www.na.org/'},
#                 {'name': 'SMART Recovery', 'description': 'Support for addiction recovery using cognitive-behavioral techniques.', 'link': 'https://www.smartrecovery.org/'},
#             ]
#         },
#         {
#             'category': 'Online Therapy Platforms',
#             'resources': [
#                 {'name': 'BetterHelp', 'description': 'Online counseling with licensed therapists.', 'link': 'https://www.betterhelp.com/'},
#                 {'name': 'Talkspace', 'description': 'Convenient online therapy sessions.', 'link': 'https://www.talkspace.com/'},
#                 {'name': 'Cerebral', 'description': 'Access to therapy and medication management.', 'link': 'https://www.cerebral.com/'},
#             ]
#         }
#     ]
    
#     return render_template('resources.html', resources=resources_list)

# @app.route('/emergency')
# def emergency():
#     # Define emergency contact information
#     emergency_contacts = {
#         'Mental Health Crisis': [
#             {'name': 'National Suicide Prevention Lifeline', 'description': '24/7 free and confidential support.', 'link': 'tel:988'},
#             {'name': 'Crisis Text Line', 'description': 'Text HOME to 741741 for free support.', 'link': 'https://www.crisistextline.org/'},
#         ],
#         'Medical Emergency': [
#             {'name': 'Emergency Services', 'description': 'Dial 911 for immediate assistance.', 'link': 'tel:911'},
#             {'name': 'Poison Control', 'description': 'Immediate help for poisoning emergencies.', 'link': 'tel:800-222-1222'},
#         ],
#         'Substance Abuse Crisis': [
#             {'name': 'SAMHSA National Helpline', 'description': '24/7 free and confidential help.', 'link': 'tel:1-800-662-HELP (4357)'},
#             {'name': 'Alcoholics Anonymous', 'description': 'Support groups for alcohol dependence.', 'link': 'https://www.aa.org/'},
#         ]
#     }
    
#     return render_template('emergency.html', contacts=emergency_contacts)

# if __name__ == '__main__':
#     try:
#         verify_env()
#         debug_mode = os.getenv('FLASK_ENV') == 'development'
#         app.run(debug=debug_mode)
#     except EnvironmentError as e:
#         print(f"Environment Error: {e}")
#         exit(1)




from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Flask app
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Verify environment variables are loaded
def verify_env():
    required_vars = ['OPENAI_API_KEY', 'FLASK_SECRET_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            "Please check your .env file and ensure all required variables are set."
        )

# Function to check content safety using OpenAI Moderation API
def is_safe(content):
    try:
        response = openai.Moderation.create(input=content)
        results = response.results[0]
        return not (results.flagged and results.categories.get('self_harm'))
    except Exception as e:
        logging.error(f"Moderation API error: {e}")
        # If moderation fails, proceed cautiously
        return False

# System message to guide the AI's responses
SYSTEM_MESSAGE = """You are a supportive mental health assistant for students. Your role is to:
1. Provide empathetic, non-judgmental responses
2. Help students find mental health resources in their area
3. Share coping strategies and self-help techniques
4. Direct users to emergency services when needed
5. Provide information about common mental health challenges students face
6. Offer resources related to medical help for injuries and mental depression.
7. When appropriate, provide names of common medications used for mental health conditions, along with a disclaimer encouraging users to consult healthcare professionals for personalized advice.
8. Always include a disclaimer such as 'Please consult a healthcare professional before starting any new medication.' when discussing medications.
"""

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').strip()
    logging.info(f"Received message: {user_message}")
    
    if not user_message:
        logging.warning("No message provided in chat.")
        return jsonify({'error': 'No message provided.'}), 400

    # Check content safety
    if not is_safe(user_message):
        logging.warning("User message flagged by moderation.")
        return jsonify({'error': 'Your message contains inappropriate content.'}), 400
    
    try:
        # Call OpenAI API using the correct method
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        ai_response = response.choices[0].message['content'].strip()
        logging.info(f"AI response: {ai_response}")
        
        # Check for crisis keywords
        crisis_keywords = [
            'suicide', 'kill myself', 'want to die', 'end it all', 
            'hurt myself', 'depression', 'self-harm', 'anxiety', 
            'panic', 'overwhelmed'
        ]
        if any(keyword in user_message.lower() for keyword in crisis_keywords):
            emergency_response = "\n\n🚨 **IMPORTANT:** If you're experiencing severe emotional distress, please reach out for immediate help:\n"
            emergency_response += "• [National Suicide Prevention Lifeline (988)](tel:988)\n"
            emergency_response += "• [Crisis Text Line: Text HOME to 741741](https://www.crisistextline.org/)\n"
            emergency_response += "• [Emergency Services: 911](tel:911)\n"
            emergency_response += "\nYou’re not alone, and help is available."
            
            ai_response += emergency_response
            logging.info("Appended emergency response due to crisis keywords.")
        
        return jsonify({'response': ai_response})
    
    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API error: {e}")
        return jsonify({'error': f"OpenAI API error: {e}"}), 500
    except Exception as e:
        logging.error(f"General error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/resources')
def resources():
    # Define a list of resources related to mental health, medical help, injuries, depression, and medications
    resources_list = [
        {
            'category': 'Mental Health Support',
            'resources': [
                {'name': 'National Alliance on Mental Illness (NAMI)', 'description': 'Education, support, and advocacy for individuals with mental illness.', 'link': 'https://www.nami.org/Home'},
                {'name': 'Depression and Bipolar Support Alliance (DBSA)', 'description': 'Support groups and resources for managing depression.', 'link': 'https://www.dbsalliance.org/'},
                {'name': 'Mental Health America (MHA)', 'description': 'Resources and information on mental health disorders.', 'link': 'https://www.mhanational.org/'},
            ]
        },
        {
            'category': 'Medical Help for Injuries',
            'resources': [
                {'name': 'Local Emergency Services', 'description': 'Dial 911 for immediate medical assistance.', 'link': 'tel:911'},
                {'name': 'Urgent Care Centers', 'description': 'Find nearby urgent care for non-life-threatening injuries.', 'link': 'https://www.urgentcare.com/'},
                {'name': 'Poison Control', 'description': 'Immediate assistance for poison-related emergencies.', 'link': 'tel:800-222-1222'},
            ]
        },
        {
            'category': 'Depression Resources',
            'resources': [
                {'name': 'SAMHSA National Helpline', 'description': '24/7, free and confidential treatment referral and information services.', 'link': 'tel:1-800-662-HELP (4357)'},
                {'name': 'National Suicide Prevention Lifeline', 'description': '24/7 free and confidential support for people in distress.', 'link': 'tel:988'},
                {'name': 'Crisis Text Line', 'description': 'Free text support available 24/7 by texting HOME to 741741.', 'link': 'https://www.crisistextline.org/'},
            ]
        },
        {
            'category': 'Substance Abuse Help',
            'resources': [
                {'name': 'Alcoholics Anonymous (AA)', 'description': 'Support groups for individuals struggling with alcohol addiction.', 'link': 'https://www.aa.org/'},
                {'name': 'Narcotics Anonymous (NA)', 'description': 'Support groups for individuals struggling with drug addiction.', 'link': 'https://www.na.org/'},
                {'name': 'SMART Recovery', 'description': 'Support for addiction recovery using cognitive-behavioral techniques.', 'link': 'https://www.smartrecovery.org/'},
            ]
        },
        {
            'category': 'Online Therapy Platforms',
            'resources': [
                {'name': 'BetterHelp', 'description': 'Online counseling with licensed therapists.', 'link': 'https://www.betterhelp.com/'},
                {'name': 'Talkspace', 'description': 'Convenient online therapy sessions.', 'link': 'https://www.talkspace.com/'},
                {'name': 'Cerebral', 'description': 'Access to therapy and medication management.', 'link': 'https://www.cerebral.com/'},
            ]
        },
        {
            'category': 'Common Medications',
            'resources': [
                {
                    'name': 'Selective Serotonin Reuptake Inhibitors (SSRIs)',
                    'description': 'Commonly prescribed for depression and anxiety.',
                    'details': [
                        {'name': 'Fluoxetine (Prozac)', 'description': 'Used to treat depression, obsessive-compulsive disorder (OCD), and other conditions.'},
                        {'name': 'Sertraline (Zoloft)', 'description': 'Effective for depression, anxiety disorders, and PTSD.'},
                        {'name': 'Escitalopram (Lexapro)', 'description': 'Prescribed for depression and generalized anxiety disorder.'},
                    ]
                },
                {
                    'name': 'Selective Norepinephrine Reuptake Inhibitors (SNRIs)',
                    'description': 'Used to treat depression and certain anxiety disorders.',
                    'details': [
                        {'name': 'Venlafaxine (Effexor)', 'description': 'Effective for major depressive disorder and anxiety.'},
                        {'name': 'Duloxetine (Cymbalta)', 'description': 'Treats depression, anxiety, and certain types of chronic pain.'},
                    ]
                },
                {
                    'name': 'Benzodiazepines',
                    'description': 'Used for short-term relief of severe anxiety and panic attacks.',
                    'details': [
                        {'name': 'Alprazolam (Xanax)', 'description': 'Used to manage anxiety and panic disorders.'},
                        {'name': 'Diazepam (Valium)', 'description': 'Used for anxiety, muscle spasms, and seizures.'},
                    ]
                },
                {
                    'name': 'Atypical Antidepressants',
                    'description': 'Used to treat depression by affecting neurotransmitters in the brain.',
                    'details': [
                        {'name': 'Bupropion (Wellbutrin)', 'description': 'Used for depression and to support smoking cessation.'},
                        {'name': 'Mirtazapine (Remeron)', 'description': 'Prescribed for depression, especially when accompanied by anxiety.'},
                    ]
                }
            ]
        }
    ]
    
    return render_template('resources.html', resources=resources_list)

@app.route('/emergency')
def emergency():
    # Define emergency contact information
    emergency_contacts = {
        'Mental Health Crisis': [
            {'name': 'National Suicide Prevention Lifeline', 'description': '24/7 free and confidential support.', 'link': 'tel:988'},
            {'name': 'Crisis Text Line', 'description': 'Text HOME to 741741 for free support.', 'link': 'https://www.crisistextline.org/'},
        ],
        'Medical Emergency': [
            {'name': 'Emergency Services', 'description': 'Dial 911 for immediate assistance.', 'link': 'tel:911'},
            {'name': 'Poison Control', 'description': 'Immediate help for poisoning emergencies.', 'link': 'tel:800-222-1222'},
        ],
        'Substance Abuse Crisis': [
            {'name': 'SAMHSA National Helpline', 'description': '24/7 free and confidential help.', 'link': 'tel:1-800-662-HELP (4357)'},
            {'name': 'Alcoholics Anonymous', 'description': 'Support groups for alcohol dependence.', 'link': 'https://www.aa.org/'},
        ]
    }
    
    return render_template('emergency.html', contacts=emergency_contacts)

if __name__ == '__main__':
    try:
        verify_env()
        debug_mode = os.getenv('FLASK_ENV') == 'development'
        app.run(debug=debug_mode)
    except EnvironmentError as e:
        print(f"Environment Error: {e}")
        exit(1)