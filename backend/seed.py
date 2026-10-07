import sys
import os

# Ensure backend directory is in python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import text
from app.database import SessionLocal, engine, Base
from app.models import Merchant, Product, ProductReview, PaymentMandate, AuditEvent
from app.aws_config import generate_text_embedding
from app.review_data import PRODUCT_REVIEWS_CATALOG


def seed_database(force_reseed=False):
    # Ensure pgvector extension is enabled on PostgreSQL
    try:
        with engine.connect() as conn:
            if engine.dialect.name == "postgresql":
                conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
                conn.commit()
    except Exception as e:
        print(f"Notice during vector extension check: {e}")

    if force_reseed:
        try:
            Base.metadata.drop_all(bind=engine)
        except Exception as e:
            print(f"Notice during drop_all: {e}")

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        if force_reseed:
            print("Force reseed requested. Clearing existing products, reviews, and merchants...")
            db.query(AuditEvent).delete()
            db.query(PaymentMandate).delete()
            db.query(ProductReview).delete()
            db.query(Product).delete()
            db.query(Merchant).delete()
            db.commit()
        else:
            existing_product = db.query(Product).first()
            if existing_product:
                print("Database already seeded. Refreshing products and reviews...")
                db.query(AuditEvent).delete()
                db.query(PaymentMandate).delete()
                db.query(ProductReview).delete()
                db.query(Product).delete()
                db.query(Merchant).delete()
                db.commit()


        merchants = [
            Merchant(name="TechMart", rating=4.8),
            Merchant(name="QuickBuy", rating=4.6),
            Merchant(name="ShopSphere", rating=4.7),
            Merchant(name="PulseGadgets", rating=4.9),
            Merchant(name="VoltAthletics", rating=4.8),
        ]

        db.add_all(merchants)
        db.commit()

        for merchant in merchants:
            db.refresh(merchant)

        m_tech = merchants[0]
        m_quick = merchants[1]
        m_shop = merchants[2]
        m_pulse = merchants[3]
        m_volt = merchants[4]

        products = [
            # -------------------------------------------------------------
            # RUNNING SHOES & FOOTWEAR (TechMart)
            # -------------------------------------------------------------
            Product(
                merchant_id=m_tech.id,
                title="Nike Revolution 6",
                price=2799,
                stock=12,
                image_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Nike",
                    "size": [8, 9, 10],
                    "color": ["Crimson Red", "Black", "Blue"],
                    "rating": 4.6,
                    "review_count": 842,
                    "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_tech.id,
                title="Adidas Runfalcon 3",
                price=2899,
                stock=8,
                image_url="https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Adidas",
                    "size": [7, 8, 9],
                    "color": ["Core Black", "Cloud White"],
                    "rating": 4.5,
                    "review_count": 612,
                    "image_url": "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-28"
            ),

            Product(
                merchant_id=m_tech.id,
                title="Puma Flyer Runner",
                price=3199,
                stock=10,
                image_url="https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Puma",
                    "size": [8, 9, 10],
                    "color": ["Shadow Grey", "Puma Black"],
                    "rating": 4.4,
                    "review_count": 420,
                    "image_url": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_tech.id,
                title="ASICS Gel Contend",
                price=2999,
                stock=5,
                image_url="https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "ASICS",
                    "size": [8, 9, 10],
                    "color": ["Electric Blue", "French Blue"],
                    "rating": 4.7,
                    "review_count": 389,
                    "image_url": "https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-29"
            ),

            Product(
                merchant_id=m_tech.id,
                title="Reebok Energen Lite",
                price=2499,
                stock=7,
                image_url="https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Reebok",
                    "size": [7, 8, 9],
                    "color": ["Vector Navy", "Core Black"],
                    "rating": 4.3,
                    "review_count": 274,
                    "image_url": "https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-30"
            ),

            # -------------------------------------------------------------
            # RUNNING SHOES & FOOTWEAR (QuickBuy)
            # -------------------------------------------------------------
            Product(
                merchant_id=m_quick.id,
                title="Nike Downshifter 12",
                price=2699,
                stock=6,
                image_url="https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Nike",
                    "size": [8, 9],
                    "color": ["Anthracite Black", "Volt"],
                    "rating": 4.5,
                    "review_count": 519,
                    "image_url": "https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_quick.id,
                title="Adidas Galaxy 7",
                price=2599,
                stock=9,
                image_url="https://images.unsplash.com/photo-1515955656352-a1fa3ffcd111?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Adidas",
                    "size": [7, 8, 9, 10],
                    "color": ["Royal Blue", "Carbon Black"],
                    "rating": 4.4,
                    "review_count": 341,
                    "image_url": "https://images.unsplash.com/photo-1515955656352-a1fa3ffcd111?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-28"
            ),

            Product(
                merchant_id=m_quick.id,
                title="Puma Softride Enzo",
                price=2999,
                stock=4,
                image_url="https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Puma",
                    "size": [9, 10],
                    "color": ["High Rise Grey", "Neon Lime"],
                    "rating": 4.6,
                    "review_count": 482,
                    "image_url": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-29"
            ),

            Product(
                merchant_id=m_quick.id,
                title="Skechers Go Run",
                price=2799,
                stock=3,
                image_url="https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Skechers",
                    "size": [8, 9],
                    "color": ["Charcoal Black", "Cyan Glow"],
                    "rating": 4.5,
                    "review_count": 290,
                    "image_url": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_quick.id,
                title="New Balance Fresh Foam",
                price=3299,
                stock=5,
                image_url="https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "New Balance",
                    "size": [9, 10],
                    "color": ["Eclipse Blue", "Silver"],
                    "rating": 4.7,
                    "review_count": 520,
                    "image_url": "https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-28"
            ),

            # -------------------------------------------------------------
            # RUNNING SHOES & FOOTWEAR (ShopSphere)
            # -------------------------------------------------------------
            Product(
                merchant_id=m_shop.id,
                title="Nike Revolution 7",
                price=2899,
                stock=15,
                image_url="https://images.unsplash.com/photo-1514989940723-e8e51635b782?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Nike",
                    "size": [8, 9, 10],
                    "color": ["Triple White", "Black Gold"],
                    "rating": 4.8,
                    "review_count": 910,
                    "image_url": "https://images.unsplash.com/photo-1514989940723-e8e51635b782?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_shop.id,
                title="Adidas Duramo SL",
                price=2799,
                stock=11,
                image_url="https://images.unsplash.com/photo-1587563871167-1ee9c731aefb?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Adidas",
                    "size": [8, 9],
                    "color": ["Core Black", "Silver Metallic"],
                    "rating": 4.6,
                    "review_count": 480,
                    "image_url": "https://images.unsplash.com/photo-1587563871167-1ee9c731aefb?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-28"
            ),

            Product(
                merchant_id=m_shop.id,
                title="Puma Velocity Nitro",
                price=3499,
                stock=6,
                image_url="https://images.unsplash.com/photo-1605348532760-6753d2c43329?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Puma",
                    "size": [9, 10],
                    "color": ["Neon Orange", "Puma Black"],
                    "rating": 4.8,
                    "review_count": 630,
                    "image_url": "https://images.unsplash.com/photo-1605348532760-6753d2c43329?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_shop.id,
                title="ASICS Gel Excite",
                price=2899,
                stock=9,
                image_url="https://images.unsplash.com/photo-1560769629-975ec94e6a86?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "ASICS",
                    "size": [8, 9, 10],
                    "color": ["Island Blue", "Gunmetal"],
                    "rating": 4.6,
                    "review_count": 395,
                    "image_url": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-29"
            ),

            Product(
                merchant_id=m_shop.id,
                title="Reebok Floatride",
                price=2699,
                stock=2,
                image_url="https://images.unsplash.com/photo-1575537302964-96cd47c06b1b?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Reebok",
                    "size": [9],
                    "color": ["Black Cyan", "Pure Grey"],
                    "rating": 4.5,
                    "review_count": 215,
                    "image_url": "https://images.unsplash.com/photo-1575537302964-96cd47c06b1b?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            # -------------------------------------------------------------
            # EXPANDED E-COMMERCE PRODUCTS (PulseGadgets & VoltAthletics)
            # -------------------------------------------------------------
            Product(
                merchant_id=m_volt.id,
                title="Nike Air Zoom Pegasus 40",
                price=3899,
                stock=14,
                image_url="https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Nike",
                    "size": [8, 9, 10, 11],
                    "color": ["Laser Blue", "Obsidian"],
                    "rating": 4.9,
                    "review_count": 1250,
                    "image_url": "https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_volt.id,
                title="Under Armour HOVR Sonic 6",
                price=3299,
                stock=8,
                image_url="https://images.unsplash.com/photo-1582588678413-dbf45f4823e9?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "running_shoes",
                    "brand": "Under Armour",
                    "size": [8, 9, 10],
                    "color": ["Jet Black", "Pitch Grey"],
                    "rating": 4.7,
                    "review_count": 410,
                    "image_url": "https://images.unsplash.com/photo-1582588678413-dbf45f4823e9?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-28"
            ),

            Product(
                merchant_id=m_pulse.id,
                title="Sony WH-CH520 Wireless Bluetooth Headphones",
                price=2999,
                stock=18,
                image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "headphones",
                    "brand": "Sony",
                    "size": ["Standard"],
                    "color": ["Matte Black", "Cream Beige"],
                    "rating": 4.8,
                    "review_count": 2100,
                    "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_pulse.id,
                title="boAt Airdopes 141 ANC True Wireless",
                price=1699,
                stock=25,
                image_url="https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "headphones",
                    "brand": "boAt",
                    "size": ["Universal"],
                    "color": ["Space Black", "Emerald Green"],
                    "rating": 4.5,
                    "review_count": 3400,
                    "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_pulse.id,
                title="JBL Tune 510BT Pure Bass On-Ear",
                price=2499,
                stock=12,
                image_url="https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "headphones",
                    "brand": "JBL",
                    "size": ["Standard"],
                    "color": ["Deep Blue", "Pure Black"],
                    "rating": 4.6,
                    "review_count": 1820,
                    "image_url": "https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-28"
            ),

            Product(
                merchant_id=m_pulse.id,
                title="Noise ColorFit Pro 5 AMOLED Smartwatch",
                price=2999,
                stock=16,
                image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "smartwatch",
                    "brand": "Noise",
                    "size": ["45mm"],
                    "color": ["Jet Black", "Silver Mesh"],
                    "rating": 4.7,
                    "review_count": 1490,
                    "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_pulse.id,
                title="Fire-Boltt Gladiator Bluetooth Calling Watch",
                price=2199,
                stock=20,
                image_url="https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "smartwatch",
                    "brand": "Fire-Boltt",
                    "size": ["1.96 Inch"],
                    "color": ["Dark Chrome", "Steel Grey"],
                    "rating": 4.4,
                    "review_count": 980,
                    "image_url": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-28"
            ),

            Product(
                merchant_id=m_pulse.id,
                title="Amazfit Bip 5 Ultra Smartwatch",
                price=3499,
                stock=7,
                image_url="https://images.unsplash.com/photo-1510017803434-a899398421b3?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "smartwatch",
                    "brand": "Amazfit",
                    "size": ["1.91 Inch"],
                    "color": ["Soft Black", "Cream White"],
                    "rating": 4.7,
                    "review_count": 720,
                    "image_url": "https://images.unsplash.com/photo-1510017803434-a899398421b3?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-29"
            ),

            # -------------------------------------------------------------
            # SNEAKERS & CASUAL FOOTWEAR
            # -------------------------------------------------------------
            Product(
                merchant_id=m_shop.id,
                title="Puma Smash v2 Leather Sneakers",
                price=2399,
                stock=14,
                image_url="https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "sneakers",
                    "brand": "Puma",
                    "size": [8, 9, 10],
                    "color": ["White/Navy", "Triple Black"],
                    "rating": 4.6,
                    "review_count": 890,
                    "image_url": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-28"
            ),

            Product(
                merchant_id=m_shop.id,
                title="Converse Chuck Taylor All Star Street",
                price=2899,
                stock=9,
                image_url="https://images.unsplash.com/photo-1607522370275-f14206abe5d3?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "sneakers",
                    "brand": "Converse",
                    "size": [7, 8, 9, 10],
                    "color": ["Classic Black", "Optical White"],
                    "rating": 4.8,
                    "review_count": 1420,
                    "image_url": "https://images.unsplash.com/photo-1607522370275-f14206abe5d3?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_volt.id,
                title="Adidas Grand Court Baseline Sneakers",
                price=2799,
                stock=11,
                image_url="https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "sneakers",
                    "brand": "Adidas",
                    "size": [8, 9, 10, 11],
                    "color": ["Core Black", "Cloud White"],
                    "rating": 4.7,
                    "review_count": 1130,
                    "image_url": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-29"
            ),

            # -------------------------------------------------------------
            # ATHLETIC & COMMUTER BAGS
            # -------------------------------------------------------------
            Product(
                merchant_id=m_quick.id,
                title="Arctic Fox Slope 30L Tech Backpack",
                price=1899,
                stock=20,
                image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "bags",
                    "brand": "Arctic Fox",
                    "size": ["30L"],
                    "color": ["Charcoal Black", "Navy Blue"],
                    "rating": 4.7,
                    "review_count": 650,
                    "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),

            Product(
                merchant_id=m_volt.id,
                title="Wildcraft Athleisure Gym & Duffle Bag",
                price=1499,
                stock=16,
                image_url="https://images.unsplash.com/photo-1547949003-9792a18a2601?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "bags",
                    "brand": "Wildcraft",
                    "size": ["35L"],
                    "color": ["Matte Grey", "Volt Lime"],
                    "rating": 4.6,
                    "review_count": 480,
                    "image_url": "https://images.unsplash.com/photo-1547949003-9792a18a2601?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-28"
            ),

            Product(
                merchant_id=m_shop.id,
                title="Skybags Tech Commuter Laptop Backpack",
                price=2299,
                stock=15,
                image_url="https://images.unsplash.com/photo-1622560480605-d83c853bc5c3?auto=format&fit=crop&w=700&q=80",
                attributes={
                    "category": "bags",
                    "brand": "Skybags",
                    "size": ["28L"],
                    "color": ["Obsidian Black", "Olive Green"],
                    "rating": 4.8,
                    "review_count": 910,
                    "image_url": "https://images.unsplash.com/photo-1622560480605-d83c853bc5c3?auto=format&fit=crop&w=700&q=80"
                },
                delivery_eta="2026-08-27"
            ),
        ]

        db.add_all(products)
        db.commit()

        print(f"Base products created ({len(products)}). Generating Amazon Bedrock Titan embeddings and seeding 10+ reviews per product...")

        total_reviews_seeded = 0
        embeddings_generated = 0

        for p in products:
            db.refresh(p)

            # Generate 1024-dimension Amazon Bedrock Titan Text Embedding
            text_to_embed = (
                f"Product: {p.title}. Category: {p.attributes.get('category', '')}. "
                f"Brand: {p.attributes.get('brand', '')}. "
                f"Colors: {', '.join(str(c) for c in p.attributes.get('color', [])) if isinstance(p.attributes.get('color'), list) else ''}. "
                f"Sizes: {', '.join(str(s) for s in p.attributes.get('size', [])) if isinstance(p.attributes.get('size'), list) else ''}. "
                f"Price: ₹{p.price:.0f}. Delivery ETA: {p.delivery_eta}."
            )

            try:
                emb = generate_text_embedding(text_to_embed)
                if emb and len(emb) == 1024:
                    p.embedding = emb
                    embeddings_generated += 1
            except Exception as e:
                print(f"Notice: Bedrock embedding skipped for '{p.title}': {e}")

            # Populate 10+ authentic reviews for this product
            reviews_list = PRODUCT_REVIEWS_CATALOG.get(p.title, [])
            for rev in reviews_list:
                db_rev = ProductReview(
                    product_id=p.id,
                    author=rev["author"],
                    rating=rev["rating"],
                    sentiment=rev["sentiment"],
                    sentiment_score=rev["sentiment_score"],
                    comment=rev["comment"],
                    aspects=rev.get("aspects"),
                    verified_purchase=rev.get("verified_purchase", True),
                    created_at=rev.get("created_at", "2026-08-01"),
                )
                db.add(db_rev)
                total_reviews_seeded += 1

        db.commit()

        print(
            f"Seed completed successfully! "
            f"{len(merchants)} merchants, {len(products)} products, "
            f"{embeddings_generated} vector embeddings, and {total_reviews_seeded} customer reviews seeded."
        )

    finally:
        db.close()



if __name__ == "__main__":
    force = "--force" in sys.argv or "-f" in sys.argv
    seed_database(force_reseed=True)