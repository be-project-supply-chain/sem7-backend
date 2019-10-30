from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS 
import numpy as np
import pickle


app = Flask(__name__)
app.config["DEBUG"] = True
loaded_model1 = pickle.load(open("model1.sav", "rb"))
loaded_model2 = pickle.load(open("model2.sav", "rb"))
CORS(app)

symptoms_dict = {
    "abdominal_pain": 39,
    "abnormal_menstruation": 101,
    "acidity": 8,
    "acute_liver_failure": 44,
    "altered_sensorium": 98,
    "anxiety": 16,
    "back_pain": 37,
    "belly_pain": 100,
    "blackheads": 123,
    "bladder_discomfort": 89,
    "blister": 129,
    "blood_in_sputum": 118,
    "bloody_stool": 61,
    "blurred_and_distorted_vision": 49,
    "breathlessness": 27,
    "brittle_nails": 72,
    "bruising": 66,
    "burning_micturition": 12,
    "chest_pain": 56,
    "chills": 5,
    "cold_hands_and_feets": 17,
    "coma": 113,
    "congestion": 55,
    "constipation": 38,
    "continuous_feel_of_urine": 91,
    "continuous_sneezing": 3,
    "cough": 24,
    "cramps": 65,
    "dark_urine": 33,
    "dehydration": 29,
    "depression": 95,
    "diarrhoea": 40,
    "dischromic _patches": 102,
    "distention_of_abdomen": 115,
    "dizziness": 64,
    "drying_and_tingling_lips": 76,
    "enlarged_thyroid": 71,
    "excessive_hunger": 74,
    "extra_marital_contacts": 75,
    "family_history": 106,
    "fast_heart_rate": 58,
    "fatigue": 14,
    "fluid_overload": 45,
    "fluid_overload.1": 117,
    "foul_smell_of urine": 90,
    "headache": 31,
    "high_fever": 25,
    "hip_joint_pain": 79,
    "history_of_alcohol_consumption": 116,
    "increased_appetite": 104,
    "indigestion": 30,
    "inflammatory_nails": 128,
    "internal_itching": 93,
    "irregular_sugar_level": 23,
    "irritability": 96,
    "irritation_in_anus": 62,
    "itching": 0,
    "joint_pain": 6,
    "knee_pain": 78,
    "lack_of_concentration": 109,
    "lethargy": 21,
    "loss_of_appetite": 35,
    "loss_of_balance": 85,
    "loss_of_smell": 88,
    "malaise": 48,
    "mild_fever": 41,
    "mood_swings": 18,
    "movement_stiffness": 83,
    "mucoid_sputum": 107,
    "muscle_pain": 97,
    "muscle_wasting": 10,
    "muscle_weakness": 80,
    "nausea": 34,
    "neck_pain": 63,
    "nodal_skin_eruptions": 2,
    "obesity": 67,
    "pain_behind_the_eyes": 36,
    "pain_during_bowel_movements": 59,
    "pain_in_anal_region": 60,
    "painful_walking": 121,
    "palpitations": 120,
    "passage_of_gases": 92,
    "patches_in_throat": 22,
    "phlegm": 50,
    "polyuria": 105,
    "prominent_veins_on_calf": 119,
    "puffy_face_and_eyes": 70,
    "pus_filled_pimples": 122,
    "receiving_blood_transfusion": 111,
    "receiving_unsterile_injections": 112,
    "red_sore_around_nose": 130,
    "red_spots_over_body": 99,
    "redness_of_eyes": 52,
    "restlessness": 20,
    "runny_nose": 54,
    "rusty_sputum": 108,
    "scurring": 124,
    "shivering": 4,
    "silver_like_dusting": 126,
    "sinus_pressure": 53,
    "skin_peeling": 125,
    "skin_rash": 1,
    "slurred_speech": 77,
    "small_dents_in_nails": 127,
    "spinning_movements": 84,
    "spotting_ urination": 13,
    "stiff_neck": 81,
    "stomach_bleeding": 114,
    "stomach_pain": 7,
    "sunken_eyes": 26,
    "sweating": 28,
    "swelled_lymph_nodes": 47,
    "swelling_joints": 82,
    "swelling_of_stomach": 46,
    "swollen_blood_vessels": 69,
    "swollen_extremeties": 73,
    "swollen_legs": 68,
    "throat_irritation": 51,
    "toxic_look_(typhos)": 94,
    "ulcers_on_tongue": 9,
    "unsteadiness": 86,
    "visual_disturbances": 110,
    "vomiting": 11,
    "watering_from_eyes": 103,
    "weakness_in_limbs": 57,
    "weakness_of_one_body_side": 87,
    "weight_gain": 15,
    "weight_loss": 19,
    "yellow_crust_ooze": 131,
    "yellow_urine": 42,
    "yellowing_of_eyes": 43,
    "yellowish_skin": 32,
}

lifestyle_symptoms_dict={ 
    'hours_walk_in_a_day':1, 
    'walk_to_workplace':2, 
    'smoking':3, 
    'drinking_alchohol':4, 
    'hours_sit':5,
    'sit_straight':6, 
    'cushioned_chair_to_sit':7, 
    'sit_in_front_of_computer':8, 
    'walk_after_lunch_dinner':9, 
    'exercise':10, 
    'outdoor_games':11, 
    'junk_food':12, 
    'eight_hours_sleep':13, 
    'eat_fruits_vegetables':14, 
    'talk_with_friends_family':15, 
    'hours_spend_on_social_media':16,
    'stress_personal_life_work_life':17,
    'sit_in_traffic_jam':18,
    'use_headphones_or_earphones_constantly':19, 
    'drink_water_in_a_day':20, 
    'headache':21, 
    'depression':22, 
    'carry_heavy_weights':23, 
    'tiredness':24, 
    'limit_sugar_and-sallt_intake':25, 
    }

lifestyle_disease_dict={    1: 'Mental illness', 
                    2: 'Back Pain',
                    3: 'Stroke',
                    4: 'atherosclerosis', 
                    5: 'Obesity', 
                    6: 'Cirrhosis', 
                    7: 'Cancer', 
                    8: 'Heart Disease', 
                    9: 'High Blood Pressure', 
                    10: 'Type-II Diabetes', 
                    11: "Alzheimer's disease", 
                    12: 'Arthritis', 
                    13: 'Atherosclerosis', 
                    14: 'Asthma', 
                    15: 'Chronic obstructive pulmonary disease', 
                    16: 'Metabolic syndrome', 
                    17: 'Chronic renal failure ', 
                    18: 'Osteoporosis', 
                    19: 'Swimmerâ\x80\x99s ear', 
                    20: 'Nephritis', 
                    21: 'Eye Pain'
                    
                }

treatment_dict={
    "Mental illness":[
        "Stick to your treatment plan. Don't skip therapy sessions. Even if you're feeling better, don't skip your medications. If you stop, symptoms may come back. And you could have withdrawal-like symptoms if you stop a medication too suddenly. If you have bothersome drug side effects or other problems with treatment, talk to your doctor before making changes",
        "Avoid alcohol and drug use. Using alcohol or recreational drugs can make it difficult to treat a mental illness. If you're addicted, quitting can be a real challenge. If you can't quit on your own, see your doctor or find a support group to help you.",
        "Stay active. Exercise can help you manage symptoms of depression, stress and anxiety. Physical activity can also counteract the effects of some psychiatric medications that may cause weight gain. Consider walking, swimming, gardening or any form of physical activity that you enjoy. Even light physical activity can make a difference",
        "Don't make important decisions when your symptoms are severe Avoid decision-making when you're in the depth of mental illness symptoms, since you may not be thinking clearly."
        "Determine priorities. You may reduce the impact of your mental illness by managing time and energy. Cut back on obligations when necessary and set reasonable goals. Give yourself permission to do less when symptoms are worse. You may find it helpful to make a list of daily tasks or use a planner structure your time and stay organized"
        "Learn to adopt a positive attitude. Focusing on the positive things in your life can make your life better and may even improve your health. Try to accept changes when they occur, and keep problems in perspective. Stress management techniques, including relaxation methods, may help"]
    # "Back Pain":
    # "Stroke":
    # "atherosclerosis":
    # "Obesity":
    # "Cirrhosis":
    # "Cancer":
    # "Heart Disease":
    # "High Blood Pressure":
    # "Type-II Diabetes":

}
@app.route("/disease",methods =['POST'])
def home():
    
    input_vector1 = np.zeros(len(symptoms_dict))
    symp = []
    data=request.json
    symptoms = data["symptoms"]
    lifestyle = data["lifestyle"] 
    # print(symptoms)

    for symptom in symptoms:
        print(symptoms_dict[symptom])
        symp.append(symptoms_dict[symptom])

    input_vector1[symp] = 1

    input_vector2 = np.zeros(25)
    symp = []
    for symptom in lifestyle:
        print(lifestyle_symptoms_dict[symptom])
        symp.append(lifestyle_symptoms_dict[symptom])
    input_vector2[symp] = 1
    d={
        "symptom_disease":loaded_model1.predict([input_vector1])[0],
        "lifestyle_disease":lifestyle_disease_dict[loaded_model2.predict([input_vector2])[0]]
        
    }
    return jsonify(d)
@app.route("/",methods=['GET'])
def h1():
    return jsonify({"message":"API fetched"})

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

