import streamlit as st

st.title('calculator')

n1 = st.number_input('Enter the First number')
n2 = st.number_input('Enter the Second number')

operator = st.text_input('Enter the operator')

if operator == '+':
    st.write(n1+n2)
elif operator=='-':
    st.write(n1-n2)
elif operator=='*':
    st.write(n1*n2)
elif operator=='/':
    st.write(n1/n2)
elif operator=='**':
    st.write(n1**n2)
elif operator=='//':
    st.write(n1//n2)
else:
    st.write('Enter correct operator')
