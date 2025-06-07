import streamlit as st
import time

st.set_page_config(page_title='EMI Caclulator', layout = 'centered')
st.title('EMI Calculator with Eligibility Check')

salary = st.number_input('💼 Enter monthly salary (₹)', min_value = 0)
loan_amount = st.number_input('💰 Enter Loan Amount (₹)', min_value = 0)
Interest_rate = st.number_input('📈 Interest rate (% per annum)', min_value = 0)
loan_years = st.number_input('📅 Loan tenure (in years)', min_value = 0)

if st.button('Check Eligibility & Calculate EMI'):
    with st.spinner('Checking Eligibility...'):
        time.sleep(2)
        if salary < 20000:
            st.error('🚫Salary is too low for eligibility')
        elif salary*12 < 300000:
            st.error('🚫Annual salary is less than 3lakhs, Not eligible for loan')
        else:
            try:
                p = loan_amount
                r = Interest_rate/12/100
                t = loan_years*12
                emi = round(p * r * (1 + r)**t / ((1 + r)**t - 1),2)
                st.success('✅ You are eligible for loan')
                st.markdown(f'### 🎯Your monthly EMI is : ₹{emi}')
            except: 
                st.error('Something went wrong! please check inputs')
