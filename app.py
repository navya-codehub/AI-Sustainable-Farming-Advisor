import streamlit as st
from pathlib import Path
import joblib


# =========================================================
# LOAD TRAINED ML MODEL
# =========================================================

model = joblib.load("crop_recommendation_model.pkl")


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Sustainable Farming Advisor",
    page_icon="🌱",
    layout="wide"
)


# =========================================================
# LOAD PROFESSIONAL CSS
# =========================================================

css_file = Path("style.css")

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# =========================================================
# TITLE
# =========================================================

st.title("🌱 AI-Powered Sustainable Farming Advisor")

st.write(
    "A decision-support tool that provides sustainable farming "
    "guidance based on crop, season, weather, soil and irrigation conditions."
)

st.info(
    "ℹ️ This prototype supports farmers with data-based advisory guidance. "
    "It does not replace qualified agricultural experts."
)


# =========================================================
# FARM INFORMATION
# =========================================================

st.header("🚜 Farm Information")

col1, col2 = st.columns(2)


with col1:

    crop = st.selectbox(
        "Select Current / Planned Crop",
        [
            "Rice",
            "Wheat",
            "Maize",
            "Sugarcane",
            "Chilli",
            "Tomato",
            "Cotton",
            "Groundnut"
        ]
    )

    season = st.selectbox(
        "Select Season",
        [
            "Kharif",
            "Rabi",
            "Zaid"
        ]
    )


with col2:

    farm_area = st.number_input(
        "Farm Area (Hectares)",
        min_value=0.1,
        max_value=1000.0,
        value=1.0,
        step=0.1
    )

    irrigation = st.selectbox(
        "Irrigation Method",
        [
            "Drip",
            "Sprinkler",
            "Flood",
            "Rainfed"
        ]
    )


# =========================================================
# FARM CONDITIONS
# =========================================================

st.header("🌦️ Farm Conditions")

col1, col2, col3 = st.columns(3)


with col1:

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=5000.0,
        value=800.0,
        step=10.0
    )

    temperature = st.number_input(
        "Average Temperature (°C)",
        min_value=-10.0,
        max_value=60.0,
        value=25.0,
        step=0.5
    )


with col2:

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=1.0
    )

    soil_ph = st.number_input(
        "Soil pH",
        min_value=3.0,
        max_value=10.0,
        value=6.5,
        step=0.1
    )


with col3:

    soil_moisture = st.number_input(
        "Soil Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=30.0,
        step=1.0
    )

    nitrogen = st.number_input(
        "Nitrogen (N) kg/ha",
        min_value=0.0,
        max_value=500.0,
        value=50.0,
        step=1.0
    )


# =========================================================
# SOIL NUTRIENT INFORMATION
# =========================================================

st.subheader("🧪 Soil Nutrient Information")

col1, col2 = st.columns(2)


with col1:

    phosphorus = st.number_input(
        "Phosphorus (P) kg/ha",
        min_value=0.0,
        max_value=500.0,
        value=30.0,
        step=1.0
    )


with col2:

    potassium = st.number_input(
        "Potassium (K) kg/ha",
        min_value=0.0,
        max_value=500.0,
        value=40.0,
        step=1.0
    )


# =========================================================
# GENERATE ADVISORY BUTTON
# =========================================================

st.divider()

generate = st.button(
    "🌱 Generate Sustainable Farming Advice",
    type="primary"
)


# =========================================================
# GENERATE RESULTS
# =========================================================

if generate:

    # =====================================================
    # MACHINE LEARNING CROP RECOMMENDATION
    # =====================================================

    ml_input = [[
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        soil_ph,
        rainfall
    ]]

    predicted_crop = model.predict(ml_input)[0]

    st.subheader("🤖 AI Crop Suitability Recommendation")

    st.info(
        f"🌾 **Current / Planned Crop:** {crop}\n\n"
        f"🤖 **AI Recommended Crop:** {predicted_crop.title()}"
    )

    st.caption(
        "The AI recommendation is generated independently from the selected "
        "crop using N, P, K, temperature, humidity, soil pH and rainfall."
    )

    st.caption(
        "Model: Random Forest classifier trained on the Crop Recommendation dataset."
    )


    # =====================================================
    # SOIL pH ASSESSMENT
    # =====================================================

    if 5.5 <= soil_ph <= 7.5:

        ph_guidance = (
            "Soil pH is within a generally suitable range for many crops."
        )

    elif soil_ph < 5.5:

        ph_guidance = (
            "Soil is acidic. Consider soil testing and appropriate "
            "soil amendments based on expert recommendations."
        )

    else:

        ph_guidance = (
            "Soil is alkaline. Conduct soil testing and follow "
            "recommended soil-management practices."
        )


    # =====================================================
    # SOIL MOISTURE ASSESSMENT
    # =====================================================

    if soil_moisture < 20:

        moisture_guidance = (
            "Soil moisture is low. Irrigation may be required, "
            "while avoiding unnecessary water use."
        )

    elif soil_moisture > 60:

        moisture_guidance = (
            "Soil moisture is high. Avoid over-irrigation and "
            "monitor drainage to reduce waterlogging."
        )

    else:

        moisture_guidance = (
            "Soil moisture is in a moderate range. Continue monitoring "
            "soil moisture before irrigation."
        )


    # =====================================================
    # AI FARMING ADVISORY
    # =====================================================

    st.header("🤖 AI Farming Advisory")

    st.success(
        "Advisory generated successfully based on the entered farm conditions."
    )


    # =====================================================
    # CROP AND SOIL ASSESSMENT
    # =====================================================

    st.subheader("🌾 Crop & Soil Assessment")

    st.write(f"**Current / Planned Crop:** {crop}")

    st.write(f"**Season:** {season}")

    st.write(
        f"**Farm Area:** {farm_area:.2f} hectares"
    )

    st.write(
        f"**Soil pH:** {soil_ph:.1f}"
    )

    st.write(
        f"**Soil Assessment:** {ph_guidance}"
    )


    # =====================================================
    # FERTILIZER AND SOIL GUIDANCE
    # =====================================================

    st.subheader("🌱 Fertilizer & Soil Guidance")

    st.write(
        f"**Soil pH Assessment:** {ph_guidance}"
    )

    st.write(
        f"**Soil Moisture Assessment:** {moisture_guidance}"
    )


    # -----------------------------------------------------
    # NITROGEN GUIDANCE
    # -----------------------------------------------------

    if nitrogen < 40:

        nitrogen_guidance = (
            "Nitrogen level appears low. Use soil-test results "
            "to determine the appropriate nitrogen application."
        )

    elif nitrogen <= 100:

        nitrogen_guidance = (
            "Nitrogen level is in a moderate range. Avoid "
            "unnecessary nitrogen application."
        )

    else:

        nitrogen_guidance = (
            "Nitrogen level is relatively high. Avoid excessive "
            "nitrogen fertilization and verify with soil testing."
        )


    # -----------------------------------------------------
    # PHOSPHORUS GUIDANCE
    # -----------------------------------------------------

    if phosphorus < 20:

        phosphorus_guidance = (
            "Phosphorus level appears low. Consider phosphorus "
            "management based on soil-test recommendations."
        )

    elif phosphorus <= 60:

        phosphorus_guidance = (
            "Phosphorus level is in a moderate range. Apply only "
            "the recommended amount based on crop requirements."
        )

    else:

        phosphorus_guidance = (
            "Phosphorus level is relatively high. Avoid unnecessary "
            "phosphorus application."
        )


    # -----------------------------------------------------
    # POTASSIUM GUIDANCE
    # -----------------------------------------------------

    if potassium < 30:

        potassium_guidance = (
            "Potassium level appears low. Follow soil-test "
            "recommendations for potassium management."
        )

    elif potassium <= 80:

        potassium_guidance = (
            "Potassium level is in a moderate range. Maintain "
            "balanced nutrient management."
        )

    else:

        potassium_guidance = (
            "Potassium level is relatively high. Avoid unnecessary "
            "potassium application."
        )


    # -----------------------------------------------------
    # FERTILIZER RECOMMENDATION
    # -----------------------------------------------------

    if soil_moisture < 20:

        fertilizer_recommendation = (
            "Improve soil moisture management before applying large "
            "amounts of fertilizer. Use soil-test results to determine "
            "the required dose."
        )

    elif soil_ph < 5.5 or soil_ph > 7.5:

        fertilizer_recommendation = (
            "Test and manage soil pH before applying large amounts "
            "of fertilizer. Avoid unnecessary fertilizer application."
        )

    else:

        fertilizer_recommendation = (
            "Use balanced fertilizer according to crop requirements "
            "and verified soil-test results. Apply nutrients at "
            "appropriate crop stages."
        )


    st.write(
        f"**Nitrogen (N) Guidance:** {nitrogen_guidance}"
    )

    st.write(
        f"**Phosphorus (P) Guidance:** {phosphorus_guidance}"
    )

    st.write(
        f"**Potassium (K) Guidance:** {potassium_guidance}"
    )

    st.write(
        f"**Fertilizer Recommendation:** {fertilizer_recommendation}"
    )


    st.success(
        "🌿 Sustainable fertilizer practice: Use soil testing, avoid "
        "over-fertilization, apply nutrients according to crop requirements, "
        "and prefer efficient nutrient management."
    )

    st.caption(
        "Responsible AI: Fertilizer guidance is decision-support information "
        "and should not replace advice from qualified agricultural experts."
    )


    # =====================================================
    # WATER MANAGEMENT
    # =====================================================

    st.subheader("💧 Water Management")


    if irrigation == "Drip":

        water_message = (
            "Drip irrigation can improve water-use efficiency. "
            "Schedule irrigation according to soil moisture and crop needs."
        )

    elif irrigation == "Sprinkler":

        water_message = (
            "Sprinkler irrigation can provide controlled water application. "
            "Avoid irrigation during strong winds or unnecessary rainfall."
        )

    elif irrigation == "Flood":

        water_message = (
            "Flood irrigation can use more water. Consider efficient "
            "irrigation methods where practical and avoid over-irrigation."
        )

    else:

        water_message = (
            "Rainfed farming depends on rainfall. Monitor soil moisture "
            "and conserve available water through suitable soil practices."
        )


    if rainfall < 400:

        rainfall_message = (
            "Rainfall is relatively low. Monitor soil moisture and plan "
            "irrigation carefully if water is available."
        )

    elif rainfall > 1500:

        rainfall_message = (
            "Rainfall is relatively high. Monitor drainage and avoid "
            "unnecessary irrigation."
        )

    else:

        rainfall_message = (
            "Rainfall is within a moderate range. Continue monitoring "
            "weather and soil moisture."
        )


    st.write(
        f"**Irrigation Method:** {irrigation}"
    )

    st.write(
        f"**Recommendation:** {water_message}"
    )

    st.write(
        f"**Rainfall Assessment:** {rainfall_message}"
    )


    # =====================================================
    # DISEASE AND PEST RISK AWARENESS
    # =====================================================

    st.subheader("🐛 Disease & Pest Risk Awareness")


    if humidity >= 75 and temperature >= 20:

        risk_message = (
            "Higher humidity combined with warm temperature may increase "
            "the possibility of certain crop diseases. Monitor crops regularly."
        )

        risk_level = "Higher environmental risk conditions"

    elif humidity >= 60:

        risk_message = (
            "Moderate-to-high humidity is present. Monitor crops for early "
            "signs of fungal diseases and pests."
        )

        risk_level = "Moderate environmental risk conditions"

    else:

        risk_message = (
            "Current humidity conditions indicate relatively lower "
            "environmental disease risk. Continue regular crop monitoring."
        )

        risk_level = "Relatively lower environmental risk conditions"


    st.write(
        f"**Humidity:** {humidity:.1f}%"
    )

    st.write(
        f"**Environmental Risk Indicator:** {risk_level}"
    )

    st.write(
        f"**Risk Guidance:** {risk_message}"
    )

    st.caption(
        "Note: This is an environmental risk-awareness indicator, "
        "not a diagnosis of a specific crop disease or pest."
    )


    # =====================================================
    # SUSTAINABLE FARMING PRACTICES
    # =====================================================

    st.subheader("♻️ Sustainable Farming Practices")

    recommendations = [

        "Use water-efficient irrigation whenever practical.",

        "Avoid unnecessary fertilizer and pesticide application.",

        "Use soil testing to guide nutrient management.",

        "Monitor crops regularly for early signs of pests and diseases.",

        "Maintain appropriate soil moisture instead of over-irrigating.",

        "Prefer environmentally responsible and resource-efficient "
        "farming practices.",

        "Maintain good drainage to reduce waterlogging.",

        "Use locally appropriate agricultural practices and expert advice."

    ]


    for recommendation in recommendations:

        st.write("• " + recommendation)


    # =====================================================
    # FARM CONDITION SUMMARY
    # =====================================================

    st.subheader("📊 Farm Condition Summary")

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Rainfall",
            f"{rainfall:.0f} mm"
        )


    with col2:

        st.metric(
            "Temperature",
            f"{temperature:.1f} °C"
        )


    with col3:

        st.metric(
            "Humidity",
            f"{humidity:.1f}%"
        )


    with col4:

        st.metric(
            "Soil Moisture",
            f"{soil_moisture:.1f}%"
        )


    # =====================================================
    # RESPONSIBLE AI
    # =====================================================

    st.divider()

    st.subheader("🛡️ Responsible AI")

    st.write(
        """
        **Fairness:** The tool is designed to provide the same type of
        decision-support process for users based on the conditions they enter.

        **Transparency:** The crop recommendation is generated from the
        Random Forest model using N, P, K, temperature, humidity, soil pH
        and rainfall. Other advisory sections use clearly defined
        rule-based guidance.

        **Privacy:** Users should avoid entering personally identifiable
        or sensitive information.

        **Human Oversight:** Recommendations should be reviewed by farmers,
        agricultural officers or qualified agricultural experts before
        important decisions are made.

        **Limitations:** Environmental conditions can change and the model
        cannot capture every local farming condition. Model performance on
        a public dataset does not guarantee the same performance in every
        real-world farming location.
        """
    )


    # =====================================================
    # SDG ALIGNMENT
    # =====================================================

    st.divider()

    st.subheader("🌍 Sustainable Development Goals")


    st.write(
        "**SDG 2 – Zero Hunger:** Supports sustainable and productive agriculture."
    )

    st.write(
        "**SDG 6 – Clean Water and Sanitation:** Encourages efficient water use."
    )

    st.write(
        "**SDG 12 – Responsible Consumption and Production:** "
        "Promotes responsible fertilizer, pesticide and resource management."
    )

    st.write(
        "**SDG 13 – Climate Action:** Encourages climate-aware and "
        "resource-efficient farming practices."
    )


    # =====================================================
    # PROJECT AI / MODEL INFORMATION
    # =====================================================

    st.divider()

    st.subheader("🧠 AI Model Information")

    st.write(
        "**AI Technique:** Random Forest Classification"
    )

    st.write(
        "**Model Inputs:** Nitrogen, Phosphorus, Potassium, Temperature, "
        "Humidity, Soil pH and Rainfall"
    )

    st.write(
        "**Training Dataset:** Crop Recommendation Dataset"
    )

    st.write(
        "**Dataset Size:** 2,200 records"
    )

    st.write(
        "**Test Set:** 440 records"
    )

    st.write(
        "**Test Accuracy:** 99.55%"
    )

    st.caption(
        "The reported accuracy was obtained on the held-out test set used "
        "during model development. It should not be interpreted as guaranteed "
        "real-world accuracy."
    )


    # =====================================================
    # FINAL DISCLAIMER
    # =====================================================

    st.divider()

    st.warning(
        "⚠️ This tool provides decision-support guidance only. "
        "Always verify recommendations with soil tests, local weather "
        "conditions and qualified agricultural experts."
    )


# =========================================================
# FOOTER
# =========================================================

st.caption(
    "AI-Powered Sustainable Farming Advisor | "
    "SDG 2 • SDG 6 • SDG 12 • SDG 13"
)