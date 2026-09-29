from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(
    title="RELMUN REX API",
    version="1.1.0"
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
# REQUEST MODEL
# =========================================================

class ChatRequest(BaseModel):
    message: str


# =========================================================
# COMMITTEE DATA
# =========================================================

COMMITTEES = {
    "unsc": {
        "name": "United Nations Security Council",
        "short": "UNSC",
        "description": "International peace and security, diplomacy and high-level decision making."
    },
    "unhrc": {
        "name": "United Nations Human Rights Council",
        "short": "UNHRC",
        "description": "Human rights, international cooperation and policy-focused debate."
    },
    "unodc": {
        "name": "United Nations Office on Drugs and Crime",
        "short": "UNODC",
        "description": "International cooperation against organised crime, drugs and related challenges."
    },
    "aippm": {
        "name": "All India Political Parties Meet",
        "short": "AIPPM",
        "description": "Parliamentary debate, political negotiation and national policy deliberation."
    },
    "unw": {
        "name": "UN Women",
        "short": "UNW",
        "description": "Gender equality, empowerment and international policy discussions."
    },
    "ipla": {
        "name": "IPL Auction",
        "short": "IPLA",
        "description": "Strategic bidding, team management and high-pressure decision making."
    }
}


# =========================================================
# RESPONSE FUNCTION
# =========================================================

def get_response(question: str) -> str:

    q = question.lower().strip()

    # =====================================================
    # GREETINGS
    # =====================================================

    greetings = [
        "hi",
        "hello",
        "hey",
        "yo",
        "sup",
        "hiya",
        "heyy",
        "heyyy"
    ]

    if q in greetings or any(q.startswith(word + " ") for word in greetings):

        return """Hey! 👋

I'm **REX**, the official **RELMUN '26** assistant.

I can help you with:

- **The conference**
- **Committees**
- **The organising team**
- **Executive Board**
- **MUNFLOW**
- **Contact information**

What would you like to know?"""


    # =====================================================
    # ABOUT RELMUN
    # =====================================================

    if (
        "what is relmun" in q
        or "what's relmun" in q
        or "tell me about relmun" in q
        or "about relmun" in q
        or "what is relmun 26" in q
        or "what's relmun 26" in q
        or "tell me about the conference" in q
        or "about the conference" in q
        or "conference details" in q
        or "more info" in q
        or "more information" in q
    ):

        return """## RELMUN '26

**RELMUN '26** stands for **Regional Engagement & Leadership Model United Nations**.

It is a **two-day online Model United Nations conference** built around diplomacy, strategy, engagement and leadership.

### Conference Details

- **Dates:** 26–27 December 2026
- **Format:** Online
- **Committees:** 6

RELMUN brings delegates together for debate, negotiation, collaboration and strategic decision-making."""


    # =====================================================
    # DATES
    # =====================================================

    if (
        "when is relmun" in q
        or "when is the conference" in q
        or "what date is relmun" in q
        or "date of relmun" in q
        or "dates of relmun" in q
        or "date" in q
        or "dates" in q
    ):

        return """**RELMUN '26** will take place on **26–27 December 2026**.

It is a **fully online** conference."""


    # =====================================================
    # ONLINE / VENUE
    # =====================================================

    if (
        "online" in q
        or "offline" in q
        or "venue" in q
        or "where is relmun" in q
        or "where will relmun" in q
        or "location" in q
    ):

        return """RELMUN '26 is a **fully online conference**.

The conference will take place on **26–27 December 2026**."""


    # =====================================================
    # MUNFLOW
    # =====================================================

    if (
        "munflow" in q
        or "technology partner" in q
        or "platform partner" in q
        or "technology and platform" in q
    ):

        return """## MUNFLOW

**MUNFLOW** is the **Technology & Platform Partner** for **RELMUN '26**.

MUNFLOW supports the technology and platform infrastructure for the conference.

The official MUNFLOW website link will be added to RELMUN once the link is provided."""


    # =====================================================
    # COMMITTEE — INDIVIDUAL
    # =====================================================

    # UNSC
    if (
        "unsc" in q
        or "security council" in q
        or "united nations security council" in q
    ):

        return """## UNSC

**United Nations Security Council**

International peace and security, diplomacy and high-level decision making.

**Committee:** UNSC"""


    # UNHRC
    if (
        "unhrc" in q
        or "human rights council" in q
        or "united nations human rights council" in q
    ):

        return """## UNHRC

**United Nations Human Rights Council**

Human rights, international cooperation and policy-focused debate.

**Committee:** UNHRC"""


    # UNODC
    if (
        "unodc" in q
        or "drugs and crime" in q
        or "drugs & crime" in q
        or "office on drugs" in q
    ):

        return """## UNODC

**United Nations Office on Drugs and Crime**

International cooperation against organised crime, drugs and related challenges.

**Committee:** UNODC"""


    # AIPPM
    if (
        "aippm" in q
        or "all india political parties" in q
        or "political parties" in q
    ):

        return """## AIPPM

**All India Political Parties Meet**

Parliamentary debate, political negotiation and national policy deliberation.

**Committee:** AIPPM"""


    # UNW
    if (
        q == "unw"
        or "un women" in q
        or "unwomen" in q
        or "women committee" in q
    ):

        return """## UN Women

**UN Women**

Gender equality, empowerment and international policy discussions.

**Committee:** UNW"""


    # IPLA
    if (
        "ipla" in q
        or "ipl auction" in q
        or "ipl auction committee" in q
    ):

        return """## IPLA

**IPL Auction**

Strategic bidding, team management and high-pressure decision making.

**Committee:** IPLA"""


    # =====================================================
    # ALL COMMITTEES
    # =====================================================

    if (
        "committee" in q
        or "committees" in q
        or "rooms" in q
        or "what are the committees" in q
        or "list the committees" in q
        or "which committees" in q
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

**05 · UNW**  
UN Women — gender equality, empowerment and international policy discussions.

**06 · IPLA**  
IPL Auction — strategic bidding, team management and high-pressure decision making."""


    # =====================================================
    # CORE TEAM
    # =====================================================

    if (
        "core team" in q
        or "who is in core" in q
        or "core members" in q
        or q == "core"
    ):

        return """## RELMUN '26 — Core

The **Core** organising team consists of:

- **Akshith Kabilan** — Secretary-General
- **S. Shreyaas** — Deputy Secretary-General
- **Laasya Vikram** — Director-General
- **Aashi Kushwaha** — Chief Advisor

The Core team leads the overall organisation and direction of RELMUN '26."""


    # =====================================================
    # SECRETARIAT
    # =====================================================

    if (
        "secretariat" in q
        or "secretariat team" in q
        or "who is in the secretariat" in q
        or "secretariat members" in q
    ):

        return """## RELMUN '26 — Secretariat

The **Secretariat** consists of:

- **Abimayur R** — Head of Administration & Outreach
- **Madhav Bhardwaj** — USG · Delegate Affairs

The Secretariat supports the operational and administrative side of RELMUN '26."""


    # =====================================================
    # COMPLETE TEAM
    # =====================================================

    if (
        "team" in q
        or "organising team" in q
        or "organizing team" in q
        or "organising committee" in q
        or "organizing committee" in q
        or "who runs relmun" in q
        or "who organises relmun" in q
        or "who organizes relmun" in q
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


    # =====================================================
    # SECRETARY-GENERAL
    # =====================================================

    if (
        "secretary general" in q
        or "secretary-general" in q
        or "sec gen" in q
        or "sec-gen" in q
    ):

        return """The **Secretary-General of RELMUN '26 is Akshith Kabilan**.

The Secretary-General is part of the **Core** organising team."""


    # =====================================================
    # DEPUTY SECRETARY-GENERAL
    # =====================================================

    if (
        "deputy secretary general" in q
        or "deputy secretary-general" in q
        or "dsg" in q
    ):

        return """The **Deputy Secretary-General of RELMUN '26 is S. Shreyaas**.

The Deputy Secretary-General is part of the **Core** organising team."""


    # =====================================================
    # DIRECTOR-GENERAL
    # =====================================================

    if (
        "director general" in q
        or "director-general" in q
        or "dg" in q
    ):

        return """The **Director-General of RELMUN '26 is Laasya Vikram**.

The Director-General is part of the **Core** organising team."""


    # =====================================================
    # CHIEF ADVISOR
    # =====================================================

    if (
        "chief advisor" in q
        or "chief adviser" in q
    ):

        return """The **Chief Advisor of RELMUN '26 is Aashi Kushwaha**.

The Chief Advisor is part of the **Core** organising team."""


    # =====================================================
    # ABIMAYUR
    # =====================================================

    if "abimayur" in q:

        return """**Abimayur R** is the **Head of Administration & Outreach** for RELMUN '26.

Abimayur is part of the **Secretariat**."""


    # =====================================================
    # MADHAV
    # =====================================================

    if "madhav" in q:

        return """**Madhav Bhardwaj** is the **USG · Delegate Affairs** for RELMUN '26.

Madhav is part of the **Secretariat**."""


    # =====================================================
    # EXECUTIVE BOARD
    # =====================================================

    if (
        "executive board" in q
        or "executive board members" in q
        or "eb members" in q
        or q == "eb"
        or "chair" in q
        or "chairs" in q
    ):

        return """## Executive Board

The **Executive Board** is responsible for guiding debate and maintaining committee procedure.

The EB lineup for the six committees is currently being finalised.

You can check the official **EB** page for updates."""


    # =====================================================
    # CONTACT
    # =====================================================

    if (
        "contact" in q
        or "email" in q
        or "instagram" in q
        or "reach relmun" in q
        or "contact relmun" in q
        or "how can i contact" in q
    ):

        return """## Contact RELMUN

**Email:**  
relmun.official@gmail.com

**Instagram:**  
@relmun.official

For official conference updates and announcements, follow **@relmun.official** on Instagram."""


    # =====================================================
    # THANKS
    # =====================================================

    if (
        "thank you" in q
        or "thanks" in q
        or q == "thank"
        or "thx" in q
    ):

        return """You're welcome! 😎

If you have anything else about **RELMUN '26**, just ask."""


    # =====================================================
    # DEFAULT
    # =====================================================

    return """I can help you with **RELMUN '26**.

Try asking:

- **"Tell me about RELMUN."**
- **"What committees are there?"**
- **"Tell me about UNSC."**
- **"Who is the Secretary-General?"**
- **"Who is in the Core?"**
- **"Who is in the Secretariat?"**
- **"Who is MUNFLOW?"**
- **"Who is on the Executive Board?"**
- **"How can I contact RELMUN?"**

Ask away — I'm **REX**. 🤖"""


# =========================================================
# API ROUTES
# =========================================================

@app.get("/")
def root():

    return {
        "status": "online",
        "service": "RELMUN REX API"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    return {
        "reply": get_response(request.message)
    }
