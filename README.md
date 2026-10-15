<div align="center">

# 🌐 Meridian
### *Autonomous AI Buyer with Bounded Mandates, pgvector Semantic Intelligence & Cryptographic Payment Verification*

**Razorpay AI Buildathon — Track 01 (Autonomous Agentic Commerce)**

<br/>

> ### 🚀 **LIVE DEMO & APPLICATION LINKS**
> ### 👉 [**https://razorpay-buildathon-sid.onrender.com**](https://razorpay-buildathon-sid.onrender.com) 👈
>
> ⚡ **Interactive Backend Swagger API Docs**: [https://razorpay-buildathon-sid-1.onrender.com/docs](https://razorpay-buildathon-sid-1.onrender.com/docs)
>
> ℹ️ *Note: The application was previously hosted on an AWS EC2 instance (`54.226.74.223`), which is currently turned off to save cloud costs. The full application is live 24/7 on Render CDN & Cloud Edge above, and can be redeployed to any EC2 instance in 1-click via `./deploy.sh`.*

<br/>

[![Live Frontend (Render)](https://img.shields.io/badge/LIVE%20DEMO-Render%20Cloud%20Edge-0066FF?style=for-the-badge&logo=render)](https://razorpay-buildathon-sid.onrender.com)
[![Backend Swagger](https://img.shields.io/badge/Backend%20API-Swagger%20Docs-10B981?style=for-the-badge&logo=fastapi)](https://razorpay-buildathon-sid-1.onrender.com/docs)
[![AWS EC2 Deployable](https://img.shields.io/badge/AWS%20EC2-1--Click%20Deployable-FF9900?style=for-the-badge&logo=amazon-aws)](./deploy.sh)
[![pgvector & RDS](https://img.shields.io/badge/pgvector-1024D%20Embeddings-336791?style=for-the-badge&logo=postgresql)](https://github.com/pgvector/pgvector)
[![AWS Bedrock](https://img.shields.io/badge/AWS%20Bedrock-Titan%20v2%20%2B%20Llama%203.3-8B5CF6?style=for-the-badge&logo=amazon-aws)](https://aws.amazon.com/bedrock/)
[![Docker Compose](https://img.shields.io/badge/Docker-Compose%20Ready-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com)
[![Razorpay Test Rails](https://img.shields.io/badge/Razorpay-Standard%20Checkout-00BAF2?style=for-the-badge&logo=razorpay)](https://razorpay.com)

<br/>

[**🌐 Live Application (Render)**](https://razorpay-buildathon-sid.onrender.com) • [**⚡ API Documentation**](https://razorpay-buildathon-sid-1.onrender.com/docs) • [**🚀 1-Click EC2 Deploy Script**](./deploy.sh) • [**📖 Render Deployment Guide**](./RENDER_DEPLOYMENT.md)

</div>

---

## 📌 Executive Summary

As autonomous AI agents evolve from conversational assistants into financial transaction engines, a critical trust and safety gap emerges: **How do we authorize AI agents to discover, evaluate, negotiate, and purchase items across multi-merchant catalogs without risking unbounded spending, hallucinations, or untrusted payments?**

**Meridian** solves this with an enterprise-grade, cloud-native **Bounded Agentic Commerce Platform**:
1. **Natural Language Intent Parsing**: Powered by AWS Bedrock (`Meta Llama 3.3 70B`) and Groq LLM to convert unstructured user queries (*"smartwatch under ₹3000 by tomorrow"*, *"marathon running shoes with responsive shock-absorbing cushion"*) into machine-readable intent mandates with strict budget, size, and ETA bounds.
2. **pgvector Semantic Search**: High-dimensional vector search utilizing **Amazon Bedrock Titan Text Embeddings v2** (`amazon.titan-embed-text-v2:0`) and PostgreSQL `pgvector` for semantic candidate matching across catalog inventory.
3. **Amazon-Style "Customers say" Review Analyzer**: AI-synthesized customer review insights with aspect satisfaction pills, itemized **Merits & Demerits**, and automated defect-detection pattern scanning across 300+ authentic verified buyer reviews.
4. **100-Point Explainable Candidate Scoring Engine**: Deterministic multi-factor mathematical evaluation (Review Sentiment 30 pts, Price Savings 25 pts, Semantic Relevance 20 pts, Merchant Reliability 15 pts, Delivery Speed 10 pts) with real-time formula transparency.
5. **Bounded Mandate Defense Engine**: Mathematically and cryptographically enforces `Candidate Amount <= Authorized Budget Ceiling` before generating single-use authorization tokens. If constraints are breached, execution safely aborts with **₹0 charged**.
6. **Single Consolidated Cart Checkout**: Bundles multiple items across different merchants into a single unified Razorpay order and tax invoice.
7. **Zero-Trust Cloud Secret Management**: Dynamic runtime credential resolution via **AWS Secrets Manager** and **AWS RDS PostgreSQL** with automated fallback to local SQLite.
8. **Live 7-Stage Cryptographic Execution Trace**: Real-time interactive stepper visualizing every stage of agent execution with expandable structured JSON payloads, cryptographic HMAC-SHA256 signature verification, and official downloadable tax invoices.

---

## 🔗 Cloud Infrastructure & Hosting Endpoints

| Component | Cloud Service / Infrastructure | Configuration / Role | Live URL / Access |
|---|---|---|---|
| 🌐 **Frontend Web Server (Render)** | **Render Static Site CDN (Active 24/7)** | React 18 + Vite SPA on global edge CDN | 👉 [**https://razorpay-buildathon-sid.onrender.com**](https://razorpay-buildathon-sid.onrender.com) |
| ⚡ **Backend API Engine (Render)** | **Render Web Service (FastAPI) (Active 24/7)** | Python 3.11 ASGI microservice on Uvicorn | 👉 [**https://razorpay-buildathon-sid-1.onrender.com**](https://razorpay-buildathon-sid-1.onrender.com) |
| 📖 **Interactive API Swagger** | **FastAPI Swagger UI (Active 24/7)** | Complete interactive API explorer and schemas | 👉 [**https://razorpay-buildathon-sid-1.onrender.com/docs**](https://razorpay-buildathon-sid-1.onrender.com/docs) |
| 🖥️ **Host Compute (IaaS)** | **AWS EC2 (Elastic Compute Cloud)** | Multi-container Docker Compose runtime (Ubuntu Linux) | *Configured & 1-Click Deployable via [`./deploy.sh`](./deploy.sh) (Instance `54.226.74.223` turned off to conserve cloud costs)* |
| 🔍 **Vector Embeddings (AI)** | **Amazon Bedrock Titan v2** | 1024-dimensional normalized text embeddings | `amazon.titan-embed-text-v2:0` |
| 🗄️ **Relational DB & Vectors** | **AWS RDS (PostgreSQL) + pgvector** | Native vector cosine similarity & catalog persistence | Connection pooling with dynamic VPC resolution |
| 🔒 **Cloud Security & Secrets** | **AWS Secrets Manager** (`ai-buyer/secrets`) | Dynamic zero-trust credential isolation via IAM roles | Encrypted at rest & in transit |
| 🧠 **Intent Mandate Model** | **AWS Bedrock** (`Llama 3.3 70B`) / Groq | Zero-assumption natural language intent parser | Serverless LLM inference |
| 💳 **Payment Rails** | **Razorpay Standard Checkout & Webhooks** | Orders API, checkout modal, HMAC-SHA256 webhooks | Live Test Rails |

---

## 🌟 Key Features

### 🛍️ 1. Split-Pane Storefront & AI Buyer Experience
- **Left Storefront Pane (~65%)**: Modern responsive e-commerce storefront with multi-category browsing (*Running, Sneakers, Audio, Watches, Bags*), live merchant filters, stock simulations, ratings, and instant *"Add to Cart"* or *"Buy with AI"*.
- **Right AI Buyer Terminal (~35%)**: Persistent conversational assistant featuring natural intent extraction, candidate ranking cards with review highlights, and two clear checkout pathways:
  - **`[Add to Cart]`**: Stashes discovered items for multi-product cart bundles.
  - **`[Proceed to Pay]`**: Dispatches the bounded agent mandate directly to Razorpay's checkout modal.

### 🔍 2. pgvector Semantic Search & Bedrock Titan Embeddings
- **1024-Dimension Semantic Search**: Replaces rigid keyword matching with high-dimensional vector cosine similarity powered by **Amazon Bedrock Titan Text Embeddings v2** (`amazon.titan-embed-text-v2:0`).
- **Cross-Dialect Vector Abstraction**: Features `CompatibleVector(1024)`—compiles to native PostgreSQL `Vector(1024)` via `pgvector` on AWS RDS PostgreSQL, while falling back gracefully to JSON vectors for offline and local testing.
- **Deep Intent Matching**: Accurately matches descriptive queries like *"marathon running shoes with responsive shock-absorbing cushion"* or *"waterproof commuter tech backpack for 16-inch macbook"* even when specific brand keywords are omitted.

### 💬 3. Amazon-Style "Customers say" Review Analyzer & Merits/Demerits
- **Catalog-Wide Review Synthesis**: Every product in Meridian's 29-item catalog is enriched with authentic customer feedback (10+ verified reviews per product, positive/neutral/negative ratings, aspect labels).
- **"Customers say" Overview Narrative**: AI-generated synthesis highlighting actual customer sentiment, common use cases, and everyday wearability.
- **Aspect Sentiment Pills**: Visual satisfaction metrics for key product dimensions (*Cushioning 92%+, Breathability 88%+, Energy Return 94%+, Fit & Width 72%+*).
- **Merits & Demerits Breakdown**: Transparent side-by-side comparison of what buyers appreciate vs potential caveats (e.g. narrow toe-boxes, initial break-in stiffness, or thin stock insoles).
- **Defect Detection Scanning**: The review engine actively scans for 8+ known defect patterns (rubbing/pinch, premature wear, sole deflation, squeaking, battery drain, sensor lag) and applies mathematical trust penalties.
- **Interactive Review Drawer**: Available both within the AI Buyer candidate cards and the Multi-Merchant Catalog Modal.

### 📊 4. 100-Point Explainable Candidate Scoring Engine
Every candidate product undergoes rigorous deterministic evaluation on a 100-point scale:

$$\text{Total Score} = S_{\text{sentiment}} (30) + S_{\text{price}} (25) + S_{\text{semantic}} (20) + S_{\text{merchant}} (15) + S_{\text{delivery}} (10)$$

| Dimension | Max Points | Evaluation Logic |
|---|---|---|
| **Review Sentiment & Trust** | **30 pts** | Positive review ratio (up to 16 pts) + sentiment intensity (up to 10 pts) + verified buyer boost (up to 4 pts) - defect penalties (up to -6 pts). |
| **Price Savings** | **25 pts** | Normalized savings ratio below user's authorized budget ceiling: $\max(0, 1 - \frac{\text{Price}}{\text{Ceiling}}) \times 25$. |
| **Semantic Match** | **20 pts** | pgvector cosine similarity between user query vector and product vector: $\text{CosineSim} \times 20$. |
| **Merchant Reliability** | **15 pts** | Verified merchant rating ratio: $(\frac{\text{Rating}}{5.0}) \times 15$. |
| **Delivery Speed** | **10 pts** | Days delivered in advance of the deadline: $\min(\frac{\text{Days Early} + 1}{7}, 1) \times 10$. |

*Discreet UI Toggle*: Users can click **"View scoring formula (+points)"** on any candidate card to inspect the exact point breakdown.

### 🛡️ 5. Bounded Mandate Security & Safety Abort
- **Strict Ceiling Enforcement**: Authorization tokens are strictly bounded to user-approved parameters.
- **Ceiling Breach Defense**: Safe abort triggers automatically if prices exceed authorized ceilings (**₹0 charged**).
- **Cryptographic Webhook Tamper Rejection**: Server-side HMAC-SHA256 signature verification rejects spoofed or altered webhook payloads with HTTP 400.
- **Stockout Auto-Recovery**: Mid-flow stockout detection with instant graceful fallback to Rank #2 candidates within mandate bounds.

### 🛒 6. Multi-Item Cart & Single Consolidated Invoice
- Persistent slide-over cart drawer with live quantity adjustments, subtotal, and tax calculations.
- **Single-Invoice Mandate Checkout**: Consolidates items from multiple merchants into **1 Razorpay Order** and **1 Single Tax Invoice**.

### 🧪 7. Built-in Prompt Studio & Architecture Inspector
- **Prompt Studio**: Built-in test harness with 1-click test scenarios (Happy Path, Open Ceiling, Budget Breach Abort, Webhook Tampering, Stockout Fallbacks).
- **Architecture Modal**: Interactive reference detailing convergence with global agentic standards (**NPCI Unified Agent Protocol / UAP**, **OpenAI/Stripe Agentic Commerce Protocol**, and **Google AP2**).

### 🧾 8. Official Tax Invoice & Append-Only Audit Trail
- **Printable & JSON Export**: Generate official Meridian tax invoices with merchant details, line items, and cryptographic signature stamps (`RCP_XXXXXX`).
- **Orders Modal**: Persistent order history tracking all past verified purchases.

---

## 🏗️ System & Cloud Architecture

```mermaid
flowchart TB
    subgraph Client["Frontend Layer (React 18 + Vite / Nginx CDN / EC2)"]
        SF["Meridian Storefront\n(Catalog & Review Drawers)"]
        Cart["Cart Drawer\n(Multi-Merchant Bundles)"]
        AgentUI["AI Buyer Agent Panel\n(Chat & Trace Stepper)"]
        Studio["Prompt Studio & Inspector"]
        Trace["Live 7-Stage Execution Trace\n(JSON Proofs)"]
    end

    subgraph Backend["Backend API Layer (FastAPI / Uvicorn)"]
        Router["FastAPI REST Endpoints\n(/api/buyer, /api/products, /api/payments)"]
        Embedder["Bedrock Titan Embedder\n(1024-dim Vector Generation)"]
        ReviewAnalyzer["Review & Sentiment Engine\n(Amazon-Style 'Customers Say')"]
        MandateEngine["Mandate Defense Guard\n(Amount <= Ceiling Check)"]
        Discovery["Multi-Merchant Scorer\n(100-Point Multi-Factor Engine)"]
        AuditEngine["Audit Logger\n(HMAC-SHA256 Signatures)"]
    end

    subgraph CloudInfra["Cloud Services & Security Layer"]
        AWS_SM["AWS Secrets Manager\n(Razorpay Keys & RDS Credentials)"]
        AWS_RDS["AWS RDS (PostgreSQL) + pgvector\n(300+ Reviews, Embeddings, Orders)"]
        AWS_Bedrock["AWS Bedrock / Groq Cloud\n(Llama 3.3 70B & Titan Text v2)"]
        RZP_Rails["Razorpay Cloud Rails\n(Orders API & HMAC Webhook)"]
    end

    SF -->|Add to Cart / Browse| Cart
    Cart -->|Consolidated Checkout| AgentUI
    Studio -->|Run Test Scenario| AgentUI
    AgentUI -->|Natural Query / Mandate| Router
    Router -->|Fetch Secrets on Boot| AWS_SM
    Router -->|Generate Query Vector| Embedder
    Embedder -->|1024D Embeddings| AWS_Bedrock
    Router -->|Vector Search & Reviews| AWS_RDS
    AWS_RDS -->|Reviews & Embeddings| ReviewAnalyzer
    ReviewAnalyzer -->|Sentiment & Aspects| Discovery
    Router -->|Scoring & Filtering| Discovery
    Discovery -->|Ranked Winner| MandateEngine
    MandateEngine -->|Check: Amount <= Ceiling| RZP_Rails
    RZP_Rails -->|Order ID & Checkout Modal| AgentUI
    RZP_Rails -->|HMAC-SHA256 Webhook| AuditEngine
    AuditEngine -->|Finalize & Lock Receipt| Trace
```

---

## ⚡ The 7-Stage Cryptographic Execution Pipeline

During every AI purchase, Meridian renders an interactive cryptographic pipeline:

| Stage | Name | Description | Verification / Payload |
|---|---|---|---|
| **1** | **Intent Parsed** | Extracts intent, category, budget ceiling, size, and ETA constraints via AWS Bedrock / Groq. | Machine-readable `IntentMandate` JSON |
| **2** | **Candidates Scored** | Discovers merchant inventory via pgvector semantic search and scores candidates on sentiment, price, merchant, and ETA. | 100-Point breakdown & Amazon-style review analysis |
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
- **Vector Search & ORM**: PostgreSQL `pgvector` with `CompatibleVector(1024)` & SQLAlchemy
- **Vector Embeddings**: Amazon Bedrock Titan Text Embeddings v2 (`amazon.titan-embed-text-v2:0`)
- **Cloud Security**: AWS Secrets Manager (`boto3`) for dynamic secret isolation
- **Database**: AWS RDS (PostgreSQL) with connection pooling / SQLite local fallback
- **LLM Engines**: AWS Bedrock Runtime (`us.meta.llama3-3-70b-instruct-v1:0`) & Groq Cloud SDK (`llama-3.3-70b-versatile` / `gpt-oss-120b`)
- **Review Intelligence**: Custom review synthesis engine with aspect sentiment extraction & defect watchouts
- **Data Validation**: Pydantic v2
- **Automation & Deployment**: Bash automated deployer (`deploy.sh`), Docker, Docker Compose

---

## 🚀 Setup & Running Options

### 🚀 Option 1: 1-Click AWS EC2 Auto-Deployment (deploy.sh)

> 💡 **Note on EC2 Status**: The project was tested and hosted on an AWS EC2 instance (`54.226.74.223`), which is currently turned off to conserve cloud costs. The live application is active 24/7 on **Render** (see Option 4). If you wish to spin up your own EC2 instance, [`deploy.sh`](./deploy.sh) automates the entire process in one command.

Meridian includes an automated deployment script [`deploy.sh`](./deploy.sh) that handles zero-configuration setup on Ubuntu/Debian or Amazon Linux EC2 instances:

```bash
# Clone the repository on your EC2 instance
git clone https://github.com/aswath-siddharth/Razorpay-Buildathon-SID-.git
cd Razorpay-Buildathon-SID-

# Make deploy script executable and run
chmod +x deploy.sh
./deploy.sh
```

**What `deploy.sh` does automatically:**
1. Verifies and installs Docker & Docker Compose v2 plugin if not already installed.
2. Synchronizes with `origin/main` git branch.
3. Automatically creates `backend/.env` template if absent.
4. Builds and launches containers in detached mode (`docker compose up -d --build`).
5. Prunes dangling images to preserve disk space.
6. Queries EC2 IMDSv2 metadata dynamically to detect and display the instance's live public IP addresses:
   - **Frontend**: `http://<YOUR_EC2_PUBLIC_IP>` (e.g. `http://54.226.74.223`)
   - **Backend API**: `http://<YOUR_EC2_PUBLIC_IP>:8000`
   - **Swagger Docs**: `http://<YOUR_EC2_PUBLIC_IP>:8000/docs`

---

### 🐳 Option 2: Run with Docker Compose Locally

Run both frontend and backend locally with a single command:

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

### 💻 Option 3: Local Manual Setup

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

# Optional AWS Integration (Secrets Manager, Bedrock & RDS PostgreSQL)
AWS_DEFAULT_REGION=us-east-1
BEDROCK_MODEL_ID=us.meta.llama3-3-70b-instruct-v1:0
# DATABASE_URL=postgresql+psycopg2://user:password@host:5432/ai_buyer
```

Seed the database with 29 products, 300+ reviews, and vector embeddings:
```bash
python seed.py --force
```

Start the backend server:
```bash
uvicorn app.main:app --reload --port 8000
```
Interactive Swagger UI will be available at `http://localhost:8000/docs`.

#### 2. Frontend Setup
```bash
cd ../frontend
npm install
npm run dev
```
Open `http://localhost:5173` in your browser.

---

### ☁️ Option 4: Automated Render Cloud Deployment

We provide a [`render.yaml`](./render.yaml) blueprint file for automated cloud deployment on [Render](https://render.com/):

1. Push your repository to GitHub.
2. In Render Dashboard, click **New +** -> **Blueprint**.
3. Select your repository. Render automatically configures the **FastAPI Web Service** and the **React Static Site CDN**.
4. Set environment variables (`RAZORPAY_KEY_SECRET`, `GROQ_API_KEY`, etc.) and click **Apply**.
5. See full instructions in [RENDER_DEPLOYMENT.md](./RENDER_DEPLOYMENT.md).

---

## 🧪 Automated Test & Verification Suites

The repository contains automated test suites to verify resilience, pgvector semantic search, and failure recovery:

### 1. Semantic Search & Review Sentiment Verification
```bash
cd backend
python test_semantic_sentiment.py
```
- Validates pgvector / Bedrock Titan vector embedding generation.
- Queries marathon running shoes and tech backpacks using natural descriptive language.
- Verifies 100-point candidate scoring, aspect pills, and Amazon-style "Customers say" synthesis.

### 2. Failure Handling & Bounded Recovery Verification
```bash
cd backend
python test_failure_recovery.py
```
- **Test 1 (Happy Path)**: End-to-end purchase execution with complete audit trail.
- **Test 2 (Mid-Flow Stockout)**: Detects mid-flow inventory depletion and gracefully falls back to Rank #2 within mandate bounds.
- **Test 3 (Retries Exhausted)**: Graceful abort with **₹0 spent** when retries are exhausted.
- **Test 4 (Live DB Stock Depletion)**: Concurrently zeroes stock in the database right before checkout reservation, verifying autonomous candidate recovery.

---

## 🎯 Test Scenarios & Demo Queries

Use these queries in the AI Buyer terminal or click them directly in **Prompt Studio**:

| Scenario | Input Query | Expected Behavior |
|---|---|---|
| **Semantic & Sentiment Discovery** | `"marathon running shoes with responsive shock absorbing cushion under 3000"` | Uses pgvector semantic search to discover top shoes, analyzes 10+ reviews, and presents Amazon-style Merits & Demerits. |
| **Happy Path Purchase** | `"running shoes under ₹3000, size 9, arrive by Friday"` | Evaluates shoes, ranks lowest price winner, authorizes mandate, and opens Razorpay Checkout modal. |
| **Open Ceiling Search** | `"I need shoes"` | Explores catalog without assuming an arbitrary budget limit, ranking top candidates by value. |
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

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

<div align="center">
Built with ❤️ for the <strong>Razorpay AI Buildathon — Track 01</strong>
</div>
