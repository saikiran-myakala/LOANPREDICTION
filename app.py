import streamlit as st
import pickle


def main():
    bg = """<div style='background-color:black; padding:13px'>
              <h1 style='color:white'>Check Loan Eligibility </h1>
       </div>"""
    st.markdown(bg, unsafe_allow_html=True)

    left, right = st.columns((2, 2))
    Gender = left.selectbox('Gender', ('Male', 'Female'))
    Married = right.selectbox('Married', ('Yes', 'No'))
    Dependents = left.selectbox('Dependents', ('None', 'One', 'Two', 'Three'))
    Education = right.selectbox('Education', ('Graduate', 'Not Graduate'))
    Self_Employed = left.selectbox('Self-Employed', ('Yes', 'No'))
    ApplicantIncome = right.number_input('Applicant Income')
    CoapplicantIncome = left.number_input('Coapplicant Income')
    LoanAmount = right.number_input('Loan Amount')
    Loan_Amount_Term = left.number_input('Loan Tenor (in months)')
    Credit_History = right.number_input('Credit History', 0.0, 1.0)
    Property_Area = st.selectbox('Property Area', ('Semiurban', 'Urban', 'Rural'))
    button = st.button('Predict')

    # if button is clicked
    if button:
        # make prediction
        result = predict(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
                         CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)
        if result == "Eligible":
            st.success(f'You are {result} for the loan')
        else:
            st.error(f'You are {result} for the loan')


# load the train model
model = pickle.load(open('./Model/train_model.pkl', 'rb'))

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "LoanPredict"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,

        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "green"},
        },
    )
if selected == "Home":
    import streamlit as st


    def set_page_style():
        st.markdown(
            """
            <style>
            /* Set the title style */
            .project-title {
                    color: black;
                    font-size:110px;
                    margin-right: -2cm;
                    font-weight: bold;
                    margin-top: 60px; 
                    font-family:Bodoni MT Black;        }

            /* Set the abstract style */
            .project-abstract {
                    color: black;
                    font-size: 20px;
                    font-weight: bold;
                    margin-top: 66px; 
                              }
            </style>
            """,
            unsafe_allow_html=True
        )


    def main():
        set_page_style()

        # Project Title
        st.markdown("<p class='project-title'>Loan Prediction</p>", unsafe_allow_html=True)

        # Project Abstract
        st.markdown(
            "<p class='project-abstract'>Welcome to the Loan Prediction app! This application uses machine learning to predict whether a user is eligible for a loan or not based on various input features, including gender, marital status, education, income, loan amount, and credit history. Simply provide your information in the input fields, click 'LoanPredict,' and the app will give you the eligibility status. It's a powerful tool to help individuals and financial institutions make informed decisions regarding loan approvals. Try it now!</p>",
            unsafe_allow_html=True)


    if __name__ == "__main__":
        main()


    def add_bg_from_url():
        st.markdown(
            f"""
             <style>
             .stApp {{
                 background-image: url("https://img.freepik.com/free-vector/indian-rupee-money-bag_23-2147988660.jpg?w=1480&t=st=1690725364~exp=1690725964~hmac=9cf677ba8c49ac1cb534e49f08c8bcbcb79a21867d73de323e150f1dbc811209");
                 background-size: cover;
             }}
             </style>
             """,
            unsafe_allow_html=True
        )


    add_bg_from_url()
if selected == "LoanPredict":
    def predict(gender, married, dependent, education, self_employed, applicant_income,
                coApplicantIncome, loanAmount, loan_amount_term, creditHistory, propertyArea):
        # processing user input
        gen = 0 if gender == 'Male' else 1
        mar = 0 if married == 'Yes' else 1
        dep = float(0 if dependent == 'None' else 1 if dependent == 'One' else 2 if dependent == 'Two' else 3)
        edu = 0 if education == 'Graduate' else 1
        sem = 0 if self_employed == 'Yes' else 1
        pro = 0 if propertyArea == 'Semiurban' else 1 if propertyArea == 'Urban' else 2
        Lam = loanAmount / 1000
        cap = coApplicantIncome / 1000
        # making predictions
        prediction = model.predict([[gen, mar, dep, edu, sem, applicant_income, cap,
                                     Lam, loan_amount_term, creditHistory, pro]])
        verdict = 'Not Eligible' if prediction == 0 else 'Eligible'
        return verdict


    if __name__ == '__main__':
        main()