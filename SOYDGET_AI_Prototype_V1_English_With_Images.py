import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="SOYDGET AI", page_icon="🌱", layout="wide")


# Images are loaded from an "images" folder beside this Python file.
IMAGE_DIR = Path(__file__).parent / "images"

MODULE_IMAGES = {
    "1. Introduction": ("okara.jpg", "Okara: soybean pulp from soymilk production"),
    "2. Halal Food": ("halal_hygiene.jpg", "Halal ingredient checks, hygiene, and safe food handling"),
    "3. Food Sustainability": ("sustainability.jpg", "Food sustainability and okara upcycling"),
    "4. Food Innovation": ("food_innovation.jpg", "Developing and evaluating an okara nugget prototype"),
    "5. Soydget Formulation": ("ai_formulation.jpg", "Digital formulation and physical validation"),
}

def show_module_image(module_name):
    """Display a module image when its matching file exists."""
    image_info = MODULE_IMAGES.get(module_name)
    if not image_info:
        return
    filename, caption = image_info
    image_path = IMAGE_DIR / filename
    if image_path.is_file():
        st.image(str(image_path), caption=caption, width="stretch")
    else:
        st.info(
            f"Image slot for {module_name}: add '{filename}' to the "
            f"'{IMAGE_DIR.name}' folder beside this Python file."
        )


MODULES = {
    "1. Introduction": "Understand okara, its production, food upcycling, sustainability, and the role of Human-AI collaboration.",
    "2. Halal Food": "Explore halal ingredient sourcing, critical control points, hygiene, cross-contamination, and food safety.",
    "3. Food Sustainability": "Explore okara upcycling, circular food systems, waste prevention, and sustainability impacts.",
    "4. Food Innovation": "Learn product design, formulation variables, ingredient functions, mass balance, and prototype evaluation.",
    "5. Soydget Formulation": "Use AI-assisted formulation predictions, document hypotheses, and prepare for physical laboratory validation.",
}

MODULE_CONTENT = {
    "2. Halal Food": {
        "intro": "Halal food development considers the permissibility of ingredients, the way materials are handled, and the cleanliness of equipment and production areas. For okara nuggets, students should check the source and status of every ingredient and avoid assuming that an ingredient is halal solely because it is plant-based.",
        "outcomes": [
            "Identify ingredients and processing aids that require halal-status verification.",
            "Explain why supplier information, labels, and certification records matter.",
            "Identify practical hygiene and cross-contamination risks during nugget preparation.",
            "Describe how halal considerations and food-safety practices can be documented."
        ],
        "sections": [
            ("2.1 Halal Ingredient Sourcing", "Review the ingredient list for okara, flour, binders, oil, seasonings, sauces, and any additives. Check product labels, supplier declarations, and relevant halal certification where applicable. If an ingredient or processing aid is unclear, flag it for verification rather than making an unsupported assumption."),
            ("2.2 Halal Critical Points", "Potential points to check include the source of flavourings and additives, the status of processing aids, storage containers, utensils, and contact surfaces. Use a simple ingredient checklist to record the item, supplier, evidence checked, and any follow-up needed. The exact control points depend on the actual recipe and production setting."),
            ("2.3 Hygiene and Food Safety", "Okara usually contains substantial moisture and can spoil quickly if mishandled. Use fresh, properly stored material; wash hands; clean and sanitise suitable work surfaces and utensils; prevent raw and cooked products from contacting one another; and cook the product thoroughly using an appropriate validated procedure."),
            ("2.4 Cross-Contamination and Allergen Awareness", "Soy is an allergen. Identify soy clearly in learning materials and product descriptions, and consider other allergens in binders, flour, seasonings, or coatings. Keep ingredients identified, use clean utensils, and communicate allergen information to anyone participating in sensory evaluation."),
            ("2.5 Student Activity: Ingredient Verification", "Choose a proposed nugget recipe. Create a table with each ingredient, its intended function, supplier or label information, halal evidence to check, allergen notes, and a status of Verified / Needs Checking. Do not label an ingredient or finished product halal without adequate evidence."),
        ],
        "quiz": [
            ("Why should students check the source and status of every ingredient?", ["All plant-based ingredients are automatically certified halal", "Ingredient status and processing information may need verification", "Ingredient checks are only needed after cooking"], 1, "Ingredient status should be verified using suitable labels, supplier information, or certification evidence."),
            ("Which is an important food-safety practice when handling okara?", ["Leave it at room temperature for an extended period", "Use clean equipment and appropriate storage", "Mix cooked product with raw ingredients using the same unclean utensil"], 1, "Okara can spoil quickly, so appropriate storage, hygiene, and separation are important."),
            ("What should students do if an ingredient's halal status is unclear?", ["Assume it is halal", "Ignore the ingredient list", "Record it as needing verification"], 2, "Record uncertainty and seek reliable evidence rather than making unsupported claims.")
        ]
    },
    "3. Food Sustainability": {
        "intro": "Food sustainability involves using resources responsibly, reducing avoidable food loss, and designing systems that make better use of materials. Okara is a useful case study because it is generated during soya processing and may be repurposed as an ingredient in new foods when quality, safety, and product suitability are considered.",
        "outcomes": [
            "Explain the meaning of food upcycling and the circular food economy.",
            "Describe how using okara may create value from a food-processing by-product.",
            "Identify environmental, practical, and economic factors that affect an upcycling idea.",
            "Propose a simple way to document material use and potential waste reduction."
        ],
        "sections": [
            ("3.1 Food Waste, By-products, and Upcycling", "A by-product is a material generated during the production of another product. Upcycling aims to give a material additional value through a suitable new use. Using okara in nuggets is one possible upcycling pathway; whether it is beneficial depends on safe handling, the recipe, processing requirements, consumer acceptance, and the alternatives available."),
            ("3.2 The Circular Food Economy", "A circular approach seeks to keep materials in productive use for as long as practical and to reduce unnecessary resource loss. In this project, students examine how okara can move from a low-value or underused stream into a food product. They should also recognise that circularity does not remove the need for food-safety controls or responsible disposal of unsuitable material."),
            ("3.3 Potential Sustainability Benefits", "Potential benefits may include better use of soy resources, reduced disposal of usable okara, and development of new product opportunities. These are potential outcomes, not guaranteed impacts. A claim such as reduced environmental impact should be supported by evidence about quantities, energy, water, packaging, transport, and the alternative use or disposal route."),
            ("3.4 Practical Constraints and Trade-offs", "Fresh okara can be wet, bulky, and perishable. Collecting, cooling, drying, transporting, or processing it may require time, energy, equipment, and cost. Students should consider whether the product is safe, acceptable, feasible to produce, and likely to use resources efficiently."),
            ("3.5 Student Activity: Okara Value Map", "Draw a simple flow: soybeans → soya processing → okara → nugget formulation → product evaluation. At each stage, identify resources used, possible losses, safety considerations, and opportunities to improve efficiency. Estimate the mass of okara used in a trial and record the basis of the calculation."),
        ],
        "quiz": [
            ("What does food upcycling mean in this project?", ["Giving a suitable by-product a useful new application", "Adding more packaging to every product", "Disposing of all by-products immediately"], 0, "Upcycling seeks to create a useful new application for a material that might otherwise be underused."),
            ("Which statement about sustainability benefits is most accurate?", ["Using okara always guarantees a lower environmental impact", "Potential benefits should be considered alongside processing, safety, and resource use", "Food safety is unrelated to sustainability"], 1, "The net benefit depends on the whole process and should not be assumed without evidence."),
            ("Why is fresh okara handling important?", ["It has no moisture", "It may be perishable and needs appropriate handling", "It never needs storage"], 1, "High moisture can make okara perishable, so suitable handling and storage matter.")
        ]
    },
    "4. Food Innovation": {
        "intro": "Food innovation turns an idea into a product that can be prepared, tested, improved, and potentially adopted by users. In the Soydget project, students develop an okara nugget prototype by considering ingredient functions, formulation proportions, processing conditions, sensory quality, and practical feasibility.",
        "outcomes": [
            "Describe the main stages of food product development.",
            "Explain the functions of key ingredients in an okara nugget formulation.",
            "Identify independent, dependent, and controlled variables in a formulation trial.",
            "Use structured observations to suggest evidence-based product improvements."
        ],
        "sections": [
            ("4.1 From Idea to Prototype", "A basic product-development cycle is: identify a need, define a target product, generate concepts, select a recipe, prepare a prototype, evaluate results, improve the formulation, and communicate findings. Students should define what success means before testing—for example, a product that holds its shape, has acceptable texture and flavour, and can be prepared consistently."),
            ("4.2 Ingredient Functions", "Okara contributes the main by-product ingredient and can influence moisture, fibre content, and structure. A binder may help ingredients hold together; flour or starch can affect structure and water absorption; water changes moisture and handling; oil can influence mouthfeel and cooking behaviour; and seasonings contribute flavour and aroma. Effects depend on the specific ingredients and process."),
            ("4.3 Formulation and Mass Balance", "Formulation records should clearly state the amount or percentage of each ingredient and the basis used for percentages. If percentages are intended to represent the total mix, they should add up to approximately 100%. If the interface uses independent sliders that do not sum to 100%, treat them as experimental input settings rather than a complete mass-balanced recipe. Record ingredient weights for reproducibility."),
            ("4.4 Experimental Design", "Change one main factor at a time for a simple introductory comparison, or use a planned design if multiple factors are tested. Keep other relevant conditions as consistent as possible, including ingredient batch, nugget size, cooking method, and evaluation procedure. Record unexpected changes instead of omitting them."),
            ("4.5 Product Evaluation and Iteration", "Assess appearance, aroma, texture, taste, and overall acceptability using a consistent evaluation form. Compare results across formulations and note the strongest and weakest attributes. Sensory results reflect the participants and test conditions; they do not by themselves establish nutritional composition, shelf life, or microbiological safety."),
            ("4.6 Student Activity: Design a Trial", "Write a product brief for an okara nugget. State the target user, desired product qualities, ingredients, one factor to vary, measurements to collect, and criteria for choosing a preferred prototype. Explain what evidence would be needed before making wider claims about nutrition, shelf life, or commercial readiness."),
        ],
        "quiz": [
            ("What is the role of a binder in many nugget formulations?", ["It may help ingredients hold together", "It guarantees food safety", "It replaces the need to measure ingredients"], 0, "A binder may support cohesion, but the effect depends on the formulation."),
            ("In a controlled formulation comparison, what should students do?", ["Change every factor without recording it", "Keep relevant conditions consistent while testing the chosen factor", "Ignore the size of each nugget"], 1, "Consistent conditions help make comparisons more meaningful."),
            ("What can a sensory test establish most directly?", ["Participants' ratings of attributes under the test conditions", "The complete shelf life of the product", "Microbiological safety without laboratory testing"], 0, "Sensory testing measures perceived attributes and acceptance, not shelf life or microbiological safety.")
        ]
    },
    "5. Soydget Formulation": {
        "intro": "This module connects digital formulation with physical testing. Students enter formulation settings into the SOYDGET AI prototype, review its illustrative predictions, state a hypothesis, prepare a physical trial under appropriate supervision, and compare predicted outputs with observed results. The current prototype uses demonstration equations, not a trained or experimentally validated machine-learning model.",
        "outcomes": [
            "Enter and document formulation settings consistently.",
            "Interpret prototype outputs as estimates for learning rather than verified product properties.",
            "Develop a testable hypothesis from a digital prediction.",
            "Compare predicted and observed results and identify limitations or next steps."
        ],
        "sections": [
            ("5.1 Digital Formulation Inputs", "The simulator provides settings for okara, binder, flour, water, oil, and seasoning. Students should record the values used, the units or percentage basis, and the reason for selecting them. Before interpreting a recipe, check whether the input values represent a complete formulation or independent demonstration settings."),
            ("5.2 Understanding the Prediction", "The prototype displays illustrative estimates for moisture, texture, aroma, and acceptability. These outputs are generated by simple demo logic and are not validated scientific measurements. They should be used to prompt questions and plan experiments, not to guarantee the quality, safety, nutrition, or consumer acceptance of a real product."),
            ("5.3 From Prediction to Hypothesis", "A prediction can be converted into a testable hypothesis. For example: 'Under the specified preparation conditions, increasing the proportion of okara may change the texture rating.' Students should identify the factor being changed, the response being measured, and the conditions to keep consistent. The direction and size of the effect must be established by data."),
            ("5.4 Physical Laboratory Validation", "Prepare trial samples using an approved recipe and safe food-handling procedures. Record ingredient weights, batch details, cooking conditions, product appearance, and sensory ratings. Use suitable supervision and procedures for cooking and tasting. Do not serve samples if ingredient history, storage, allergen information, or food safety is uncertain."),
            ("5.5 Prediction-versus-Observation Review", "Compare the digital estimate with the observed rating for the same attribute and formulation. Calculate the absolute difference where appropriate and discuss possible reasons: the demo equation, measurement variability, differences in raw materials, processing conditions, or the limits of sensory evaluation. A single comparison is not enough to validate a model."),
            ("5.6 Improving the Prototype", "A future evidence-based model would require a well-documented dataset with consistent formulation inputs and measured outputs, enough relevant samples, a suitable train/test strategy, and performance evaluation. Students should retain raw data, document exclusions, and avoid claiming model accuracy until it has been tested appropriately."),
            ("5.7 Student Activity: Formulation Validation Log", "Record: (1) formulation settings, (2) AI output, (3) hypothesis, (4) physical procedure, (5) observed sensory results, (6) difference between predicted and observed results, and (7) a reflection on what to change in the next trial."),
        ],
        "quiz": [
            ("How should students interpret the current simulator's predictions?", ["As guaranteed measurements of the finished product", "As illustrative outputs that require physical validation", "As proof of halal status"], 1, "The prototype uses demonstration equations and is not a validated ML model."),
            ("What makes a hypothesis testable?", ["It describes a relationship that can be checked with defined observations or measurements", "It cannot be measured", "It is accepted as true before testing"], 0, "A testable hypothesis identifies something that can be examined using a planned procedure and evidence."),
            ("Why is one prediction-versus-observation comparison insufficient to validate a model?", ["One trial cannot adequately establish general predictive performance", "A model never needs data", "Sensory scores are always identical"], 0, "Model validation requires sufficient data and suitable performance evaluation, not just one example.")
        ]
    }
}

if "prediction" not in st.session_state:
    st.session_state.prediction = None
if "sensory" not in st.session_state:
    st.session_state.sensory = None


def predict(okara, binder, flour, water, oil, seasoning):
    # DEMONSTRATION logic only. Not a validated ML model or a food-quality guarantee.
    moisture = np.clip(52 + 0.32 * okara + 0.22 * water - 0.12 * flour, 0, 100)
    texture = np.clip(5.2 + 0.06 * binder + 0.035 * flour - 0.025 * okara + 0.015 * oil, 1, 9)
    aroma = np.clip(5.8 + 0.025 * seasoning + 0.01 * oil - 0.008 * okara, 1, 9)
    acceptability = np.clip(0.35 * texture + 0.30 * aroma + 2.0, 1, 9)
    return moisture, texture, aroma, acceptability


def sidebar():
    st.sidebar.title("🌱 SOYDGET AI")
    st.sidebar.caption("Human-AI Collaborative Learning Platform")
    role = st.sidebar.radio("Mode", ["Student", "Lecturer"])
    st.sidebar.divider()
    st.sidebar.info("NALI 2026 Prototype\nDigitalising Okara Nugget (Soydget) Innovation")
    return role


def render_quiz(module_name, questions):
    st.markdown("### 📝 Knowledge Check")
    selected = []
    for i, (question, options, correct, explanation) in enumerate(questions):
        answer = st.radio(question, options, key=f"{module_name}_quiz_{i}")
        selected.append((answer, options[correct], explanation))
    if st.button(f"Check {module_name} Answers", key=f"{module_name}_submit", type="primary"):
        score = sum(answer == correct_answer for answer, correct_answer, _ in selected)
        st.session_state[f"{module_name}_score"] = score
        st.session_state[f"{module_name}_feedback"] = [
            (answer == correct_answer, explanation) for answer, correct_answer, explanation in selected
        ]
    score_key = f"{module_name}_score"
    if score_key in st.session_state:
        score = st.session_state[score_key]
        st.metric("Quiz Score", f"{score}/{len(questions)}")
        for i, (correct, explanation) in enumerate(st.session_state[f"{module_name}_feedback"], start=1):
            if correct:
                st.success(f"Question {i}: Correct. {explanation}")
            else:
                st.info(f"Question {i}: Review this point. {explanation}")


role = sidebar()
st.title("🌱 SOYDGET AI")
st.caption("Predict Digitally • Validate Physically • Learn Collaboratively")

if role == "Student":
    tabs = st.tabs(["🏠 Home", "📚 Learning Modules", "🤖 AI Formulation", "🧪 Sensory Validation"])

    with tabs[0]:
        st.subheader("Human-AI Collaborative Learning Journey")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Modules", "5")
        c2.metric("AI Simulation", "Ready")
        c3.metric("Sensory Scale", "9-point")
        c4.metric("Validation", "Closed-loop")
        st.markdown("""
        **Learning flow**

        `Learn → Simulate → Predict → Physical Lab → Validate → Reflect`

        The AI supports formulation decisions; students remain responsible for interpreting and validating predictions through laboratory evidence.
        """)
        st.info("Learning principle: AI outputs are decision-support examples. They do not replace food-safety checks, laboratory evidence, or lecturer guidance.")

    with tabs[1]:
        st.subheader("Five Core Learning Modules")
        st.caption("Study the learning notes, complete the activities, and check your understanding in each module.")
        for name, desc in MODULES.items():
            with st.expander(name, expanded=(name == "1. Introduction")):
                st.write(desc)
                show_module_image(name)
                if name == "1. Introduction":
                    st.markdown("## 🌱 Introduction to Okara")
                    st.write("Okara is the solid pulp left after soybeans are processed to extract soymilk. Soybeans are commonly soaked, ground with water, and filtered to separate the liquid from the solid material. The remaining pulp is called okara. It usually contains substantial moisture, so appropriate handling and storage are important for quality and safety.")
                    st.markdown("### Learning Outcomes")
                    st.write("By the end of this module, students should be able to:")
                    st.markdown("- Explain what okara is and how it is produced.\n- Identify physical characteristics such as colour, texture, moisture, and odour.\n- Suggest at least two possible food applications for okara.\n- Relate okara reuse to food sustainability and waste reduction.\n- Explain the aim of developing okara nuggets and the role of AI in learning.")
                    st.markdown("### 1. What Is Okara and How Is It Produced?")
                    st.write("Okara is a by-product of soya processing, particularly soymilk production. After soybeans are ground and filtered, the liquid is used as soymilk while the separated solid pulp becomes okara. Although it is often treated as waste, okara may still contain fibre, protein, and other food components. Its actual composition depends on the raw materials and processing method.")
                    st.info("Observation activity: Examine an okara sample and record its colour, texture, moisture, and odour. Do not taste or smell a sample unless it has been handled safely and your instructor has approved the activity.")
                    st.markdown("### 2. Potential Reuse of Soy Pulp")
                    st.write("Okara can be explored as an ingredient in products such as nuggets, food balls, bread, and biscuits. In nuggets, it may contribute fibre and protein and influence moisture and structure. Its use should be adjusted to its water content, flavour, texture, and the binding ingredients. Trials and evaluation are needed to identify a suitable formulation.")
                    st.write("**Student activity:** List three food products that could be developed using okara and explain why each product might be suitable.")
                    st.markdown("### 3. Food Sustainability and Product Innovation")
                    st.write("Food sustainability involves using resources responsibly, reducing avoidable waste, and making better use of materials. Using okara in a food product is one way to explore added value from a processing by-product. This relates to the circular food economy, in which underused materials may re-enter a value chain through suitable innovation.")
                    st.write("**Student activity:** Compare okara that is not used with okara that is processed into nuggets. What are the potential benefits and challenges of each option?")
                    st.markdown("### 4. Objectives of Developing Okara Nuggets")
                    st.write("The project aims to develop a nugget prototype that uses okara as one of its main ingredients. Students investigate how formulation changes may affect texture, taste, colour, moisture, and consumer acceptability. SOYDGET AI can help generate ideas and initial predictions from the information entered. These predictions are not experimental results and must be compared with physical observations and real data.")
                    st.success("Mini challenge: Write a hypothesis about how increasing the okara content might affect nugget texture. Explain how you would test it fairly.")
                    st.markdown("### Human-AI Collaboration")
                    st.markdown("1. **Students** identify a problem, develop hypotheses, conduct experiments, and record data.\n2. **AI** helps generate ideas, organise formulation options, and produce initial predictions.\n3. **Physical validation** compares predictions with observed results so that conclusions are based on evidence.")
                    st.warning("Food-safety note: Okara can spoil quickly because of its high moisture content. Use properly handled and stored material, practise good hygiene, cook the product thoroughly using an appropriate procedure, and account for soy and other allergens.")
                    render_quiz("Introduction", [
                        ("What is okara?", ["The liquid extracted from soybeans", "The solid pulp left after soya processing", "Oil extracted from soybeans"], 1, "Okara is the solid pulp separated during soya processing."),
                        ("Why might okara be useful in nuggets?", ["It may contribute fibre and protein and influence texture", "It guarantees every nugget will be crispier", "It removes the need for food-safety controls"], 0, "Its effects depend on the recipe and should be evaluated."),
                        ("What is the role of AI in this project?", ["Replace all physical experiments", "Automatically certify food safety", "Help generate ideas and predictions that must be tested"], 2, "AI supports learning; physical testing and evidence remain essential.")
                    ])
                else:
                    content = MODULE_CONTENT[name]
                    st.markdown("### Module Overview")
                    st.write(content["intro"])
                    st.markdown("### Learning Outcomes")
                    st.write("By the end of this module, students should be able to:")
                    st.markdown("\n".join(f"- {outcome}" for outcome in content["outcomes"]))
                    for heading, body in content["sections"]:
                        st.markdown(f"### {heading}")
                        st.write(body)
                    st.markdown("### Reflection")
                    reflection_prompts = {
                        "2. Halal Food": "Which ingredient or process step in your proposed recipe needs the most careful verification, and what evidence would you check?",
                        "3. Food Sustainability": "What potential benefit and what practical trade-off should be considered when using okara in nuggets?",
                        "4. Food Innovation": "Which formulation variable would you test first, and what measurements would help you decide whether the change improved the product?",
                        "5. Soydget Formulation": "What did the AI predict, what did the physical test show, and what could explain any difference?"
                    }
                    st.text_area("Write your reflection", placeholder=reflection_prompts[name], key=f"{name}_reflection", height=100)
                    render_quiz(name.split(". ")[0] + "_" + name.split(". ")[1].replace(" ", "_"), content["quiz"])
                st.progress(1.0 if name == "1. Introduction" else 0.75)
                st.caption("Learning content status: Prototype module")

    with tabs[2]:
        st.subheader("🤖 AI Formulation Simulator")
        st.write("Adjust formulation settings, then ask the prototype to generate illustrative estimates for selected product attributes.")
        col1, col2 = st.columns(2)
        with col1:
            okara = st.slider("Okara setting (%)", 20, 70, 45)
            binder = st.slider("Binder setting (%)", 5, 30, 15)
            flour = st.slider("Flour setting (%)", 5, 35, 20)
        with col2:
            water = st.slider("Water setting (%)", 5, 30, 12)
            oil = st.slider("Oil setting (%)", 1, 15, 8)
            seasoning = st.slider("Seasoning setting (%)", 1, 10, 5)
        st.caption("Important: These sliders are independent demo settings and may not sum to 100%. They are not a validated recipe or mass-balanced formulation.")
        if st.button("🔮 Predict Formulation", type="primary"):
            st.session_state.prediction = predict(okara, binder, flour, water, oil, seasoning)
            st.session_state.formulation_inputs = {"Okara": okara, "Binder": binder, "Flour": flour, "Water": water, "Oil": oil, "Seasoning": seasoning}
        if st.session_state.prediction:
            moisture, texture, aroma, acceptability = st.session_state.prediction
            st.divider()
            st.subheader("Illustrative Prototype Output")
            a, b, c, d = st.columns(4)
            a.metric("Estimated Moisture", f"{moisture:.1f}%")
            b.metric("Illustrative Texture", f"{texture:.1f}/9")
            c.metric("Illustrative Aroma", f"{aroma:.1f}/9")
            d.metric("Illustrative Acceptability", f"{acceptability:.1f}/9")
            st.subheader("Recorded Inputs")
            st.dataframe(pd.DataFrame([st.session_state.get("formulation_inputs", {})]), width="stretch")
            st.subheader("AI Co-Pilot Reflection")
            st.write("Use the output to form a hypothesis and plan a physical trial. Do not treat these estimates as measured product properties or as evidence of safety, nutrition, or market readiness.")
            st.warning("Prototype limitation: the current outputs use demonstration equations, not a trained or experimentally validated machine-learning model. Replace them with a model only after collecting and evaluating suitable experimental data.")

    with tabs[3]:
        st.subheader("🧪 9-Point Hedonic Sensory Validation")
        st.write("After physical preparation and only when the sample is safe for evaluation, enter observed sensory ratings. Follow your instructor's procedure and disclose relevant allergens.")
        cols = st.columns(5)
        attrs = ["Colour", "Aroma", "Texture", "Taste", "Overall Acceptability"]
        ratings = {}
        for col, attr in zip(cols, attrs):
            ratings[attr] = col.selectbox(attr, list(range(1, 10)), index=6, key=f"sensory_{attr}")
        st.caption("Suggested scale: 1 = Dislike extremely; 5 = Neither like nor dislike; 9 = Like extremely.")
        if st.button("Submit Laboratory Result", type="primary"):
            st.session_state.sensory = ratings
        if st.session_state.sensory:
            st.success("Laboratory result recorded for this session.")
            st.dataframe(pd.DataFrame([st.session_state.sensory]), width="stretch")
            if st.session_state.prediction:
                actual = st.session_state.sensory["Overall Acceptability"]
                predicted = st.session_state.prediction[3]
                st.metric("Illustrative Prediction vs Observed Rating", f"{predicted:.1f} → {actual}/9", f"Absolute difference {abs(predicted - actual):.1f}")
                st.caption("This comparison is educational only; one sample does not validate the prediction logic.")

else:
    tabs = st.tabs(["📊 Dashboard", "👩‍🎓 Student Monitoring", "🧪 Prediction vs Actual"])
    with tabs[0]:
        st.subheader("Lecturer Dashboard")
        a, b, c, d = st.columns(4)
        a.metric("Students", "32")
        b.metric("Module Completion", "86%")
        c.metric("AI Attempts", "118")
        d.metric("Intervention Alerts", "6")
        st.info("Dashboard figures below are illustrative prototype data, not live student records.")
        df = pd.DataFrame({"Module": ["Introduction", "Halal Food", "Food Sustainability", "Food Innovation", "Soydget Formulation"], "Average Score": [92, 84, 78, 87, 71]})
        st.bar_chart(df.set_index("Module"))
        st.subheader("Students Requiring Intervention")
        alerts = pd.DataFrame({"Student": ["Muhammad Umar Mukhlis", "Auni Insyirah Zaki", "Ainul Mardhiah Aqeel"], "Issue": ["Formulation calculation", "Halal critical points", "Moisture formulation"], "Status": ["Review", "Review", "Review"]})
        st.dataframe(alerts, width="stretch")
    with tabs[1]:
        st.subheader("Student Performance")
        students = pd.DataFrame({"Student": ["Nur Delisha Ahmad", "Auni Insyirah Zaki", "Ainul Mardhiah Aqeel", "Tan Sia Hong", "Omar Abdallah Jamil"], "Modules Completed": [5, 5, 4, 3, 4], "Average Score": [91, 88, 82, 61, 68], "AI Attempts": [4, 3, 5, 2, 3], "Intervention": ["No", "No", "No", "Yes", "Yes"]})
        st.caption("Illustrative sample data for interface demonstration.")
        st.dataframe(students, width="stretch")
    with tabs[2]:
        st.subheader("AI Prediction vs Physical Laboratory Validation")
        compare = pd.DataFrame({"Student": ["S001", "S002", "S003", "S004", "S005"], "AI Texture": [7.4, 6.8, 8.1, 7.2, 6.9], "Observed Texture": [7.2, 7.0, 7.5, 7.4, 6.7], "Absolute Difference": [0.2, 0.2, 0.6, 0.2, 0.2]})
        st.caption("Illustrative comparison data only; not actual experimental results.")
        st.dataframe(compare, width="stretch")
        st.line_chart(compare.set_index("Student")[["AI Texture", "Observed Texture"]])

st.divider()
st.caption("SOYDGET AI • NALI 2026 Prototype • Human-AI Collaborative Learning")
