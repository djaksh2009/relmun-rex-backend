from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(
    title="RELMUN REX API",
    version="1.0.0"
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# MODELS
# =========================================================

class ChatRequest(BaseModel):
    message: str


# =========================================================
# RELMUN DATA
# =========================================================

REGISTRATION_FEE = "₹200"

CONFERENCE_DATES = "26–27 December 2026"

CONFERENCE_MODE = "Online"


# =========================================================
# REX RESPONSE ENGINE
# =========================================================

def get_response(question: str) -> str:

    q = question.lower().strip()


    # -----------------------------------------------------
    # GREETING
    # -----------------------------------------------------

    if any(
        q.startswith(word)
        for word in [
            "hi",
            "hello",
            "hey",
            "yo",
            "sup",
            "hii",
            "heyy"
        ]
    ):

        return """Hey! 👋

I'm **REX**, the official RELMUN '26 assistant.

I can help you with:

- **RELMUN '26**
- **Committees**
- **The organising team**
- **Conference details**
- **Executive Board**
- **Registration**
- **MUNFLOW**
- **Contact information**

What would you like to know?"""


    # -----------------------------------------------------
    # REGISTRATION / FEE
    # -----------------------------------------------------

    if any(
        word in q
        for word in [
            "fee",
            "fees",
            "cost",
            "price",
            "registration fee",
            "how much",
            "register"
        ]
    ):

        return f"""## Registration

The **delegate registration fee is {REGISTRATION_FEE}**.

**RELMUN '26** will take place on **{CONFERENCE_DATES}** and will be conducted fully online.

Please check the official registration section for the registration form and opening status."""


    # -----------------------------------------------------
    # ABOUT
    # -----------------------------------------------------

    if (
        "what is relmun" in q
        or "tell me about relmun" in q
        or "about relmun" in q
        or "more info" in q
        or "more information" in q
        or "what is this" in q
    ):

        return f"""## RELMUN '26

**RELMUN '26** stands for **Regional Engagement & Leadership Model United Nations**.

It is a **two-day online Model United Nations conference** built around diplomacy, strategy, engagement and leadership.

### Conference Details

- **Dates:** {CONFERENCE_DATES}
- **Format:** {CONFERENCE_MODE}
- **Committees:** 6
- **Delegate Registration:** {REGISTRATION_FEE}

RELMUN brings delegates together for debate, negotiation, collaboration and strategic decision-making."""


    # -----------------------------------------------------
    # DATES
    # -----------------------------------------------------

    if (
        "date" in q
        or "dates" in q
        or "when is relmun" in q
        or "when is the conference" in q
    ):

        return f"""RELMUN '26 will take place on **{CONFERENCE_DATES}**.

It is a **fully online** conference."""


    # -----------------------------------------------------
    # ONLINE
    # -----------------------------------------------------

    if (
        "online" in q
        or "offline" in q
        or "physical" in q
        or "venue" in q
        or "where is relmun" in q
    ):

        return f"""RELMUN '26 is a **fully online conference**.

The conference will take place on **{CONFERENCE_DATES}**."""


    # -----------------------------------------------------
    # MUNFLOW
    # -----------------------------------------------------

    if (
        "munflow" in q
        or "technology partner" in q
        or "platform partner" in q
        or "technology and platform" in q
        or "tech partner" in q
    ):

        return """## MUNFLOW

**MUNFLOW** is the **Technology & Platform Partner** for **RELMUN '26**.

MUNFLOW provides the technology and platform infrastructure supporting the conference.

The official MUNFLOW website link will be added once it is provided to the RELMUN team."""


    # -----------------------------------------------------
    # COMMITTEES
    # -----------------------------------------------------

    if (
        "committee" in q
        or "committees" in q
        or "rooms" in q
    ):

        return """## RELMUN '26 Committees

There are **six committee experiences**:

**01 · UNSC**  
United Nations Security Council — international peace and security, diplomacy and high-level decision making.

**02 · UNHRC**  
United Nations Human Rights Council — human rights, international cooperation and policy-focused debate.

**03 · UNODC**  
United Nations Office on Drugs and Crime — international cooperation against organised crime, drugs and related challenges.

**04 · AIPPM**  
All India Political Parties Meet — parliamentary debate, political negotiation and national policy deliberation.

**05 · UN Women**  
UN Women — gender equality, empowerment and international policy discussions.

**06 · IPLA**  
IPL Auction — strategic bidding, team management and high-pressure decision making."""


    # -----------------------------------------------------
    # SPECIFIC COMMITTEES
    # -----------------------------------------------------

    committee_data = {

        "unsc": (
            "United Nations Security Council",
            "International peace and security, diplomacy and high-level decision making."
        ),

        "unhrc": (
            "United Nations Human Rights Council",
            "Human rights, international cooperation and policy-focused debate."
        ),

        "unodc": (
            "United Nations Office on Drugs and Crime",
            "International cooperation against organised crime, drugs and related challenges."
        ),

        "aippm": (
            "All India Political Parties Meet",
            "Parliamentary debate, political negotiation and national policy deliberation."
        ),

        "unw": (
            "UN Women",
            "Gender equality, empowerment and international policy discussions."
        ),

        "ipla": (
            "IPL Auction",
            "Strategic bidding, team management and high-pressure decision making."
        )

    }


    for code, data in committee_data.items():

        if code in q:

            full_name, description = data

            return f"""## {code.upper()}

**{full_name}**

{description}

You can find the detailed mandate, format and focus of this committee on the RELMUN '26 Committees page."""


    # -----------------------------------------------------
    # TEAM
    # -----------------------------------------------------

    if (
        "team" in q
        or "organising" in q
        or "organizing" in q
        or "secretariat" in q
    ):

        return """## RELMUN '26 Organising Team

### Core

- **Akshith Kabilan** — Secretary-General
- **S. Shreyaas** — Deputy Secretary-General
- **Laasya Vikram** — Director-General
- **Aashi Kushwaha** — Chief Advisor

### Secretariat

- **Abimayur R** — Head of Administration & Outreach
- **Madhav Bhardwaj** — USG · Delegate Affairs"""


    # -----------------------------------------------------
    # SECRETARY GENERAL
    # -----------------------------------------------------

    if (
        "secretary general" in q
        or "sec gen" in q
        or "sec-gen" in q
    ):

        return """The **Secretary-General of RELMUN '26 is Akshith Kabilan**.

The Secretary-General is part of the **Core** organising team."""


    # -----------------------------------------------------
    # EXECUTIVE BOARD
    # -----------------------------------------------------

    if (
        "executive board" in q
        or q == "eb"
        or "chair" in q
        or "chairs" in q
    ):

        return """## Executive Board

The **Executive Board** will be responsible for guiding debate and maintaining committee procedure.

The EB lineup for the six committees is currently being finalised.

You can check the official **EB** page for updates."""


    # -----------------------------------------------------
    # CONTACT
    # -----------------------------------------------------

    if (
        "contact" in q
        or "email" in q
        or "mail" in q
        or "instagram" in q
        or "reach" in q
        or "phone" in q
    ):

        return """## Contact RELMUN

**Email:**  
relmun.official@gmail.com

**Instagram:**  
@relmun.official

For official conference updates and announcements, follow **@relmun.official** on Instagram."""


    # -----------------------------------------------------
    # THANKS
    # -----------------------------------------------------

    if (
        "thank you" in q
        or q == "thanks"
        or q == "thank"
    ):

        return """You're welcome! 😎

If you have anything else about **RELMUN '26**, just ask."""


    # -----------------------------------------------------
    # DEFAULT
    # -----------------------------------------------------

    return """I can help you with **RELMUN '26**.

Try asking:

- **"Tell me more about the conference."**
- **"What committees are there?"**
- **"Who is the Secretary-General?"**
- **"What is the registration fee?"**
- **"Tell me about the organising team."**
- **"Who is MUNFLOW?"**
- **"What is UNSC?"**
- **"How can I contact RELMUN?"**

Ask away — I'm REX."""


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():

    return {
        "status": "online",
        "service": "RELMUN REX API",
        "version": "1.0.0"
    }


# =========================================================
# CHAT
# =========================================================

@app.post("/chat")
def chat(request: ChatRequest):

    return {
        "reply": get_response(
            request.message
        )
    }
