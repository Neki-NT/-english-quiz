import streamlit as st

def main():
    # Введение
    st.title("English Quiz Program")
    st.write("Welcome to the English Quiz!")
    st.write("Here are the words you can use to fill in the blanks:")
    
    # Новый список ответов с измененной последовательностью
    answers = [
        "violate", "vision", "volume", "valid", "welfare", "via",
        "whereby", "uniform", "unify", "widespread", "unique", "trend",
        "undergo", "undertake", "vehicle", "visual", "virtual", "underlie",
        "vary", "ultimate", "visible", "whereas", "utilise"
    ]
    st.write(", ".join(answers))
    st.write("Use each word only once to answer the questions. Let's begin!")

    # Вопросы и ответы
    questions = [
        ("The new fashion __ shows that oversized clothes are becoming popular.", "trend"),
        ("This discovery marked the __ achievement in her academic career.", "ultimate"),
        ("Students must __ a rigorous process to prepare for university.", "undergo"),
        ("The basic principles of mathematics __ many scientific theories.", "underlie"),
        ("Our team decided to __ a challenging research project this year.", "undertake"),
        ("All employees must wear a __ uniform during working hours.", "uniform"),
        ("The international conference helped scientists __ their expertise.", "unify"),
        ("This solution is __ and cannot be found anywhere else.", "unique"),
        ("It is important to properly __ available resources to maximize efficiency.", "utilise"),
        ("The results of the test were declared __ and accepted by the committee.", "valid"),
        ("The cost of living can __ significantly between urban and rural areas.", "vary"),
        ("This __ was used to transport materials to the research site.", "vehicle"),
        ("The updated __ of the software includes new features and improvements.", "version"),
        ("The researchers traveled to the conference __ multiple countries.", "via"),
        ("Plagiarism can __ the ethical rules of academic writing.", "violate"),
        ("Many students prefer to participate in __ learning sessions.", "virtual"),
        ("The results of the experiment were clearly __ to everyone present.", "visible"),
        ("The scientist had a clear __ for how the project should be completed.", "vision"),
        ("The presentation included many __ aids to help explain the topic.", "visual"),
        ("The __ of data collected during the study was impressive.", "volume"),
        ("Participation in this study is completely __ and not mandatory.", "voluntary"),
        ("The government focuses on improving the __ of its citizens through various programs.", "welfare"),
        ("The first hypothesis was proven incorrect, __ the second one was successful.", "whereas"),
        ("They implemented a system __ users can easily share their research findings.", "whereby"),
        ("The idea has gained __ recognition among academics worldwide.", "widespread"),
    ]

    score = 0
    for i, (question, correct_answer) in enumerate(questions, 1):
        user_answer = st.text_input(f"{i}. {question}", key=f"q{i}")
        if user_answer.lower() == correct_answer:
            score += 1

    if st.button("Submit"):
        st.write(f"Quiz complete! You got {score} out of {len(questions)} correct.")

if __name__ == "__main__":
    main()
