<div align="center">

# 🌐 Meridian
### *Autonomous AI Buyer with Bounded Mandates, Cloud-Native Resilience & Cryptographic Payment Verification*

**Razorpay AI Buildathon — Track 01 (Autonomous Agentic Commerce)**

<br/>

> ### 🚀 **LIVE DEMO & APPLICATION LINKS**
> ### 👉 [**https://razorpay-buildathon-sid.onrender.com**](https://razorpay-buildathon-sid.onrender.com) 👈
>
> ⚡ **Interactive Backend Swagger API Docs**: [https://razorpay-buildathon-sid-1.onrender.com/docs](https://razorpay-buildathon-sid-1.onrender.com/docs)

<br/>

[![Live Frontend](https://img.shields.io/badge/LIVE%20DEMO-https%3A%2F%2Frazorpay--buildathon--sid.onrender.com-0066FF?style=for-the-badge&logo=render)](https://razorpay-buildathon-sid.onrender.com)
[![Backend Swagger](https://img.shields.io/badge/Backend%20API-Swagger%20Docs-10B981?style=for-the-badge&logo=fastapi)](https://razorpay-buildathon-sid-1.onrender.com/docs)
[![AWS Cloud](https://img.shields.io/badge/AWS-Secrets%20Manager%20%7C%20RDS%20%7C%20Bedrock-FF9900?style=for-the-badge&logo=amazon-aws)](https://aws.amazon.com)
[![Docker](https://img.shields.io/badge/Docker-Compose%20Ready-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com)
[![Razorpay Test Rails](https://img.shields.io/badge/Razorpay-Standard%20Checkout-00BAF2?style=for-the-badge&logo=razorpay)](https://razorpay.com)
[![Groq LLM](https://img.shields.io/badge/Groq-Llama%203.3%20%2F%20GPT%20OSS-F55036?style=for-the-badge&logo=groq)](https://groq.com)

<br/>

[**🌐 Live Application**](https://razorpay-buildathon-sid.onrender.com) • [**⚡ API Documentation**](https://razorpay-buildathon-sid-1.onrender.com/docs) • [**📖 Render Deployment Guide**](./RENDER_DEPLOYMENT.md) • [**🐳 Docker Compose**](./docker-compose.yml)

</div>

---

## 📌 Executive Summary

As autonomous AI agents evolve from conversational assistants into financial transaction engines, a critical trust and safety gap emerges: **How do we authorize AI agents to discover, evaluate, negotiate, and purchase items across multi-merchant catalogs without risking unbounded spending, hallucinations, or untrusted payments?**

**Meridian** solves this with an enterprise-grade, cloud-native **Bounded Agentic Commerce Platform**:
1. **Natural Language Intent Parsing**: Powered by AWS Bedrock (`Meta Llama 3.3 70B`) and Groq LLM to convert unstructured user queries (*"smartwatch under ₹3000 by tomorrow"*, *"running shoes, size 9"*) into machine-readable intent mandates with strict budget, size, and ETA bounds.
2. **Explainable Candidate Evaluation**: Evaluates inventory across multi-merchant catalogs with real-time scoring and visible reasoning for why candidates were selected or rejected.
3. **Bounded Mandate Defense Engine**: Mathematically and cryptographically enforces `Candidate Amount <= Authorized Budget Ceiling` before generating single-use authorization tokens. If constraints are breached, execution safely aborts with **₹0 charged**.
4. **Single Consolidated Cart Checkout**: Bundles multiple items across different merchants into a single unified Razorpay order and tax invoice.
5. **Zero-Trust Cloud Secret Management**: Dynamic runtime credential resolution via **AWS Secrets Manager** and **AWS RDS PostgreSQL** with automated fallback to local SQLite.
6. **Live 7-Stage Cryptographic Execution Trace**: Real-time interactive stepper visualizing every stage of agent execution with expandable structured JSON payloads, cryptographic HMAC-SHA256 signature verification, and official downloadable tax invoices.

---

## 🔗 Cloud Infrastructure & Hosting Endpoints

| Component | Cloud Service / Infrastructure | Configuration / Role |
|---|---|---|
| 🖥️ **Host Compute (IaaS)** | **AWS EC2 (Elastic Compute Cloud)** | Multi-container Docker Compose runtime (Ubuntu/Linux) |
| 🌐 **Frontend Web Server** | **Nginx Alpine (Port 80)** | SPA Static Server & Reverse Proxy to Backend API (`/api/`) |
| ⚡ **Backend API Engine** | **FastAPI / Uvicorn (Port 8000)** | Asynchronous Python 3.11 ASGI Microservice |
| 🔒 **Cloud Security & Secrets** | **AWS Secrets Manager** (`ai-buyer/secrets`) | Dynamic zero-trust credential isolation via IAM roles |
| 🗄️ **Relational Database** | **AWS RDS (PostgreSQL)** / Local SQLite | Dynamic VPC database discovery & connection pooling |
| 🧠 **Cloud LLM Inference** | **AWS Bedrock** (`Llama 3.3 70B`) / Groq | Serverless AI Intent Mandate Parsing |
| 🌐 **Live Web Application** | AWS EC2 / Render Cloud Edge | 👉 [**https://razorpay-buildathon-sid.onrender.com**](https://razorpay-buildathon-sid.onrender.com) |
| ⚡ **Backend Swagger API Docs** | FastAPI Swagger Interactive UI | 👉 [**https://razorpay-buildathon-sid-1.onrender.com/docs**](https://razorpay-buildathon-sid-1.onrender.com/docs) |
| 📦 **GitHub Repository** | GitHub | 👉 [**aswath-siddharth/Razorpay-Buildathon-SID-**](https://github.com/aswath-siddharth/Razorpay-Buildathon-SID-) |

---

## 🌟 Key Features

### 🛍️ 1. Split-Pane Storefront & AI Buyer Experience
- **Left Storefront Pane (~65%)**: Modern responsive e-commerce storefront with multi-category browsing (*Running, Sneakers, Audio, Watches, Bags*), live merchant filters, stock simulations, ratings, and instant *"Add to Cart"* or *"Buy with AI"*.
- **Right AI Buyer Terminal (~35%)**: Persistent conversational assistant featuring natural intent extraction, explainability reasoning cards, and two clear checkout pathways:
  - **`[Add to Cart]`**: Stashes discovered items for multi-product cart bundles.
  - **`[Proceed to Pay]`**: Dispatches the bounded agent mandate directly to Razorpay's checkout modal.

### 🧠 2. Zero-Assumption Intent Parsing (AWS Bedrock & Groq)
- Extracts category, explicit budget ceilings (understands `2500`, `3k`, `₹3,000`), sizing parameters, and delivery deadlines.
- **Zero-Assumption Design**: Never invents or assumes an arbitrary budget when none is specified.
- **Resilient Multi-Provider Fallback**: Seamlessly switches between AWS Bedrock Runtime, Groq Cloud API, and local heuristic parsing during network degradation.

### 🛡️ 3. Bounded Mandate Security & Safety Abort
- **Strict Ceiling Enforcement**: Authorization tokens are strictly bounded to user-approved parameters.
- **Ceiling Breach Defense**: Safe abort triggers automatically if prices exceed authorized ceilings (₹0 charged).
- **Cryptographic Webhook Tamper Rejection**: Server-side HMAC-SHA256 signature verification rejects spoofed or altered webhook payloads (HTTP 400).
- **Stockout Auto-Recovery**: Mid-flow stockout detection with instant graceful fallback to Rank #2 candidates within mandate bounds.

### 🛒 4. Multi-Item Cart & Single Consolidated Invoice
- Persistent slide-over cart drawer with live quantity adjustments, subtotal, and tax calculations.
- **Single-Invoice Mandate Checkout**: Consolidates items from multiple merchants into **1 Razorpay Order** and **1 Single Tax Invoice**.

### 🧪 5. Built-in Prompt Studio & Architecture Inspector
- **Prompt Studio**: Built-in test harness with 1-click test scenarios (Happy Path, Open Ceiling, Budget Breach Abort, Webhook Tampering, Stockout Fallbacks).
- **Architecture Modal**: Interactive reference detailing convergence with global agentic standards (**NPCI Unified Agent Protocol / UAP**, **OpenAI/Stripe Agentic Commerce Protocol**, and **Google AP2**).

### 🧾 6. Official Tax Invoice & Append-Only Audit Trail
- **Printable & JSON Export**: Generate official Meridian tax invoices with merchant details, line items, and cryptographic signature stamps (`RCP_XXXXXX`).
- **Orders Modal**: Persistent order history tracking all past verified purchases.

---

## 🏗️ System & Cloud Architecture

```mermaid
flowchart TB
    subgraph Client["Frontend Layer (React 18 + Vite / Nginx CDN)"]
        SF["Meridian Storefront\n(Catalog & Filters)"]
        Cart["Cart Drawer\n(Multi-Item Bundles)"]
        AgentUI["AI Buyer Agent Panel\n(Chat & Trace Stepper)"]
        Studio["Prompt Studio & Inspector"]
        Trace["Live 7-Stage Execution Trace\n(JSON Proofs)"]
    end

    subgraph Backend["Backend API Layer (FastAPI / Uvicorn)"]
        Router["FastAPI REST Endpoints\n(/api/buyer, /api/payments)"]
        MandateEngine["Mandate Defense Guard\n(Amount <= Ceiling Check)"]
        Discovery["Multi-Merchant Scorer\n(Weighted Ranking Algorithm)"]
        AuditEngine["Audit Logger\n(HMAC-SHA256 Signatures)"]
    end

    subgraph CloudInfra["Cloud Services & Security Layer"]
        AWS_SM["AWS Secrets Manager\n(Razorpay Keys & RDS Secret)"]
        AWS_RDS["AWS RDS (PostgreSQL) / SQLite\n(Catalogs & Orders)"]
        AWS_Bedrock["AWS Bedrock / Groq Cloud\n(Llama 3.3 70B Intent Model)"]
        RZP_Rails["Razorpay Cloud Rails\n(Orders API & HMAC Webhook)"]
    end

    SF -->|Add to Cart / Browse| Cart
    Cart -->|Consolidated Checkout| AgentUI
    Studio -->|Run Test Scenario| AgentUI
    AgentUI -->|Natural Query / Mandate| Router
    Router -->|Fetch Secrets on Boot| AWS_SM
    Router -->|Query / Persist| AWS_RDS
    Router -->|Parse Intent| AWS_Bedrock
    Router -->|Scoring & Filtering| Discovery
    Discovery -->|Ranked Winner| MandateEngine
    MandateEngine -->|Check: Amount <= Ceiling| RZP_Rails
    RZP_Rails -->|Order ID & Checkout Modal| AgentUI
    RZP_Rails -->|HMAC-SHA256 Webhook| AuditEngine
    AuditEngine -->|Finalize & Lock Receipt| Trace
```

---

## ⚡ The 7-Stage Execution Pipeline

During every AI purchase, Meridian renders an interactive cryptographic pipeline:

| Stage | Name | Description | Verification / Payload |
|---|---|---|---|
| **1** | **Intent Parsed** | Extracts intent, category, budget ceiling, size, and ETA constraints via AWS Bedrock / Groq. | Machine-readable `IntentMandate` JSON |
| **2** | **Candidates Scored** | Discovers merchant inventory and evaluates candidates on price, rating, and stock. | Ranked candidates list & explainability score |
| **3** | **Mandate Authorized** | Proves `Amount <= Budget Ceiling`. Halts with Safe Abort if breached. | `Bounded Proof: ₹Price <= ₹Ceiling` |
| **4** | **Order Created** | Generates consolidated merchant order and itemized line items. | Single Invoice Order Payload |
| **5** | **Payment Initiated** | Dispatches Razorpay Orders API and launches reactive Checkout modal. | Razorpay Order ID & checkout trigger |
| **6** | **Webhook Verified** | Cryptographically verifies server-side HMAC-SHA256 signature payload. | `HMAC-SHA256 Signature: PASS` |
| **7** | **Confirmed** | Seals cryptographic audit log and generates official downloadable Tax Invoice. | Receipt ID (`RCP_XXXXXX`) & Locked Audit |

---

## 💻 Tech Stack

### Frontend
- **Framework**: React 18 + Vite
- **Styling**: Vanilla CSS Design System (Stripe/Fintech Dark/Light Glassmorphism)
- **Icons**: Lucide React
- **Payments SDK**: Razorpay Standard Checkout (`checkout.razorpay.com/v1/checkout.js`)
- **Web Server / Distribution**: Nginx Alpine (Docker) / Render Static Site (CDN)
- **Typography**: Outfit, Satoshi, Inter, JetBrains Mono

### Backend & Cloud Compute
- **Framework**: FastAPI (Python 3.11)
- **Server**: Uvicorn (ASGI)
- **Cloud Security**: AWS Secrets Manager (`boto3`) for dynamic secret isolation
- **Database / ORM**: AWS RDS (PostgreSQL) / SQLite via SQLAlchemy
- **LLM Engines**: AWS Bedrock Runtime (`us.meta.llama3-3-70b-instruct-v1:0`) & Groq Cloud SDK (`llama-3.3-70b-versatile` / `gpt-oss-120b`)
- **Data Validation**: Pydantic v2
- **Containerization**: Docker, Docker Compose, Multi-stage builds

---

## 🚀 Setup & Running Options

### 🐳 Option 1: Run with Docker Compose (Recommended)

Run both the frontend and backend with a single command:

```bash
# Clone the repository
git clone https://github.com/aswath-siddharth/Razorpay-Buildathon-SID-.git
cd Razorpay-Buildathon-SID-

# Start all containers
docker-compose up --build
```
* **Frontend**: `http://localhost:3000`
* **Backend API & Swagger Docs**: `http://localhost:8000/docs`

---

### 💻 Option 2: Local Manual Setup

#### Prerequisites
- Node.js (v18+) & npm
- Python (v3.10+)

#### 1. Backend Setup
```bash
cd backend
python -m venv venv

# Windows:
venv\Scripts\activate
# Linux/macOS:
# source venv/bin/activate

pip install -r requirements.txt
```

Create `backend/.env`:
```env
RAZORPAY_KEY_ID=rzp_test_TTbqDaKP2i6PmQ
RAZORPAY_KEY_SECRET=your_razorpay_secret
RAZORPAY_WEBHOOK_SECRET=your_webhook_secret
GROQ_API_KEY=your_groq_api_key

# Optional AWS Integration (Secrets Manager & Bedrock)
AWS_DEFAULT_REGION=us-east-1
BEDROCK_MODEL_ID=us.meta.llama3-3-70b-instruct-v1:0
# DATABASE_URL=postgresql+psycopg2://user:password@host:5432/dbname
```

Start the backend server:
```bash
uvicorn app.main:app --reload --port 8000
```
Swagger UI will be available at `http://localhost:8000/docs`.

#### 2. Frontend Setup
```bash
cd ../frontend
npm install
npm run dev
```
Open `http://localhost:5173` in your browser.

---

### ☁️ Option 3: Automated Render Cloud Deployment

We provide a [`render.yaml`](./render.yaml) blueprint file for automated cloud deployment on [Render](https://render.com/):

1. Push your repository to GitHub.
2. In Render Dashboard, click **New +** -> **Blueprint**.
3. Select your repository. Render automatically configures the **FastAPI Web Service** and the **React Static Site CDN**.
4. Set environment variables (`RAZORPAY_KEY_SECRET`, `GROQ_API_KEY`, etc.) and click **Apply**.
5. See full instructions in [RENDER_DEPLOYMENT.md](./RENDER_DEPLOYMENT.md).

---

## 🧪 Test Scenarios & Demo Queries

Use these queries in the AI Buyer terminal or click them directly in **Prompt Studio**:

| Scenario | Input Query | Expected Behavior |
|---|---|---|
| **Happy Path Purchase** | `"running shoes under ₹3000, size 9, arrive by Friday"` | Evaluates shoes, ranks lowest price winner, authorizes mandate, and opens Razorpay Checkout modal. |
| **Open Ceiling Search** | `"I need shoes"` | Explores sneakers without assuming an arbitrary budget limit, ranking top candidates by value. |
| **Smartwatch Discovery** | `"smartwatch under ₹3000 by tomorrow"` | Finds matching AMOLED/GPS smartwatches arriving tomorrow. |
| **Mandate Breach Abort** | `"smartwatch under 1k by tomorrow"` | Detects price exceeds ₹1,000 ceiling. Triggers **Safe Abort** (₹0 charged). |
| **Cryptographic Webhook** | Click *"Webhook Tamper"* demo | Demonstrates server-side rejection of invalid HMAC-SHA256 signatures (Status 400). |
| **Stockout Recovery** | Click *"Stockout Fallback"* demo | Simulates mid-flow stockout on Rank #1 and recovers to Rank #2 within bounds. |
| **Consolidated Cart** | Add 2+ items to Cart $\rightarrow$ Click *"Checkout Whole Cart with AI Mandate"* | Bundles all items into **1 Single Tax Invoice** and single Razorpay payment. |

---

## 🔒 Security & Mandate Guarantees

1. **Pre-Authorized Budget Bounds**: The AI agent cannot charge beyond the exact ceiling authorized in the intent mandate.
2. **Zero-Spend Mitigation**: If any parameter fails (inventory, price breach, user cancellation), the transaction aborts with ₹0 funds touched.
3. **AWS Zero-Trust Secrets Isolation**: Master keys are fetched dynamically from AWS Secrets Manager rather than being committed to version control.
4. **Cryptographic Webhook Verification**: All fulfillment relies on server-validated HMAC-SHA256 signatures, preventing man-in-the-middle replay attacks.
5. **Immutable Audit Trail**: Every decision, score, and state transition is sealed with timestamps and raw payload inspection.
