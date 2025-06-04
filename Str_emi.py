import streamlit as st
import time
st.set_page_config(page_title='EMI Calculator', layout='centered')

st.title('EMI Calculator with Eligibility check')

salary = st.number_input('💼 Enter your monthly salary (₹)', min_value=0)
loan_amount = st.number_input('💰 Enter Loan amont (₹)', min_value =0)
interest_rate = st.number_input('📈 Enter interest rate (% per annum)', min_value = 0.0)
loan_years = st.number_input('📅 Loan tenure (in years)', min_value=0)

if st.button('Check Eligibility & Calculate EMI'):
    with st.spinner('Checking Eligibility...'):
        time.sleep(2)

        if salary < 25000:
            st.error('🚫 Salary is too low for loan eligibility.')
        elif salary * 12 < 300000:
            st.error('🚫 Annual salary below ₹3,00,000. Not eligible for loan')
        else:
            try:
                p = loan_amount
                r = interest_rate/12/100
                t = loan_years * 12
                emi = round(p * r * (1 + r)**t / ((1 + r)**t - 1),2)
                st.success(f'✅You are eligible!')
                st.markdown(f'### 🎯 Your monthly emi is: ₹{emi}')
            except:
                st.error('Something went wrong!, please check inputs.')
