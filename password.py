import os 
os.system("cls")
import streamlit as st
import random,string
st.title("password")

st.header("password setting")

lower = st.checkbox("Include lower case")
upper = st.checkbox("Include upper case")
symbol = st.checkbox("Include symbol")
number = st.checkbox("Include number")
space = st.checkbox("Include space")
length = st.number_input("whats the password length?",8, 25)

settings =  {
    "lower_case" : lower,
    "upper_case" : upper,
    "symbol" : symbol,
    "number" : number,
    "space" : space,
    "length" : length
}




def random_generator_password(choice):
    random_choice = random.choice(choice)
    if random_choice == "space" :
        return " "
    if random_choice == "symbol" :
        return random.choice("+-*/=_(&)^%$#@!><:")
    if random_choice == "number":
        return random.choice("0123456789")
    if random_choice == "upper_case":
        return random.choice(string.ascii_uppercase)
    if random_choice == "lower_case":
        return random.choice(string.ascii_lowercase)


def password_generator(seting):
    final_password = ""
    password_length = settings["length"]
    choices = list(filter(lambda x: seting[x] , ["space","symbol","number","upper_case","lower_case"] ))
    for i in range(password_length):
        final_password += random_generator_password(choices)
    return final_password 

if st.button("submit"):
    frame = st.header(password_generator(settings))
