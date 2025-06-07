import streamlit as st

#page_setup
st.set_page_config(page_title = 'EMI Calculator 💰', page_icon='💸', layout = 'centered')

#page_title
st.markdown('## 🏦 EMI Calculator')
st.markdown('Calculate your monthly EMI')

#User_Inputs
st.markdown('## 🔢 Enter Loan Details: ')

col1, col2 = st.columns(2)

with col1:
    loan_amount = st.number_input('💵 Loan Amount (₹)', min_value = 0 )
with col2:
    interest_rate = st.number_input('📈 Annual Interest rate (%)', min_value = 0.0, format='%.2f')

loan_years = st.number_input('📅 Loan Tenure in (months)', min_value = 0 )

#EMI Calculation
if st.button('🧮 Calculate EMI'):
    monthly_interest = interest_rate/12/100
    emi = round(loan_amount * monthly_interest * (1 + monthly_interest)**loan_years / ((1 + monthly_interest)**loan_years - 1), 2)

    st.success(f'✅ Your monthly emi is: ₹ {emi:,.2f}')

    total_payment = emi*loan_years
    total_interest = total_payment - loan_amount

    st.markdown(f'### 📊 Loan summary')
    st.write(f'💰 Total Payment is: ₹ {total_payment:,.2f}')
    st.write(f'💸 Total interest payable is: ₹ {total_interest:,.2f}')