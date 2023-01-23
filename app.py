import streamlit as st
from smshelper import get_phone_info, selectnode

max_limit = {"sms": 1000, "call": 15, "mail": 200}

st.sidebar.title("Bombers")


bomber_options = ["SMS Bombing", "Email Bombing"]
user_bomber_select = st.sidebar.selectbox("Select Your Bombing Technique: ", options=bomber_options)


if user_bomber_select == bomber_options[0]:
    st.write(user_bomber_select)

    country_code = st.number_input("Enter Your Country Code Without + sign: ", step=1)
    phone_number = st.number_input("Enter The Phone Number: ", step=1)
    sms_count = st.number_input("Enter the number of messages you want to send (max: 500): ", step=1, min_value=1, max_value=500)
    delay = st.number_input("Enter the delay time: (min: 5)", step=1, min_value=1)
    
    threads = st.number_input("Enter Number of Thread (max: 50)", step=1)

    if st.button("Bombard"):
        status = get_phone_info(country_code, phone_number)

        if status["status"] != "valid":
            st.warning(status["message"])
        else:
            result = selectnode(str(country_code), str(phone_number), sms_count, delay, threads)
            st.success(result["status"])
            st.json(result)