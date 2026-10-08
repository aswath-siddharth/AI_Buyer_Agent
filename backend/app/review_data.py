from typing import Any

# Seed reviews data for all 29 products across Meridian catalog
# Each product has 10-12 authentic, varied reviews with sentiments: POSITIVE, NEUTRAL, NEGATIVE.

PRODUCT_REVIEWS_CATALOG = {
    # -------------------------------------------------------------------------
    # 1. Nike Revolution 6
    # -------------------------------------------------------------------------
    "Nike Revolution 6": [
        {"author": "Aarav Sharma", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.92,
         "comment": "Incredible daily road runners. The foam midsole absorbs shock nicely on morning 6K runs. Super lightweight.",
         "aspects": {"cushioning": "excellent", "weight": "lightweight"}, "verified_purchase": True, "created_at": "2026-08-02"},
        {"author": "Priya Nair", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Breathable mesh upper keeps feet dry even in humid conditions. Crimson color looks sharp.",
         "aspects": {"breathability": "high", "style": "striking"}, "verified_purchase": True, "created_at": "2026-07-28"},
        {"author": "Rohan Patel", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.82,
         "comment": "Great value for a Nike running shoe under ₹3000. Outsole traction has held up for 250+ kilometers.",
         "aspects": {"durability": "good", "value": "great"}, "verified_purchase": True, "created_at": "2026-07-22"},
        {"author": "Siddharth Jain", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.74,
         "comment": "Good cushioning for jogging. Slightly stiff during the first two runs but broke in comfortably.",
         "aspects": {"comfort": "good", "break_in": "needed"}, "verified_purchase": True, "created_at": "2026-07-19"},
        {"author": "Ananya Roy", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.91,
         "comment": "Fits true to size UK 8. Very stable heel counter with no slippage when sprinting.",
         "aspects": {"fit": "true_to_size", "stability": "high"}, "verified_purchase": True, "created_at": "2026-07-15"},
        {"author": "Vikram Sen", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.15,
         "comment": "Decent pair for treadmill, but the insole padding is rather thin if you have flat feet.",
         "aspects": {"insole": "thin", "arch_support": "average"}, "verified_purchase": True, "created_at": "2026-07-10"},
        {"author": "Neha Kulkarni", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.70,
         "comment": "Comfortable ankle padding and nice laces that stay tied. Satisfied with the purchase.",
         "aspects": {"comfort": "good", "laces": "secure"}, "verified_purchase": True, "created_at": "2026-07-05"},
        {"author": "Manish Verma", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.05,
         "comment": "Average running shoe. Looks better in pictures than in person, but works fine for walking.",
         "aspects": {"aesthetic": "average", "comfort": "moderate"}, "verified_purchase": False, "created_at": "2026-06-29"},
        {"author": "Kavita Rao", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Very flexible sole and comfortable toe box. Perfect for college commute and evening cardio.",
         "aspects": {"flexibility": "high", "toe_box": "roomy"}, "verified_purchase": True, "created_at": "2026-06-22"},
        {"author": "Deepak Menon", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.72,
         "comment": "Runs noticeably narrow on wide feet. Felt pinching on my pinky toe after a 4km jog.",
         "aspects": {"fit": "too_narrow", "discomfort": "blisters"}, "verified_purchase": True, "created_at": "2026-06-18"},
        {"author": "Aditya Joshi", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.83,
         "comment": "Light and springy. Excellent road grip even on wet asphalt.",
         "aspects": {"grip": "excellent", "responsiveness": "springy"}, "verified_purchase": True, "created_at": "2026-06-12"},
    ],

    # -------------------------------------------------------------------------
    # 2. Adidas Runfalcon 3
    # -------------------------------------------------------------------------
    "Adidas Runfalcon 3": [
        {"author": "Tanmay Deshmukh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Cloudfoam cushioning makes these super plush for walking and casual 5K runs.",
         "aspects": {"cushioning": "plush", "comfort": "high"}, "verified_purchase": True, "created_at": "2026-08-01"},
        {"author": "Meera Iyer", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.76,
         "comment": "Classic Adidas three-stripe styling in Core Black. Very clean look and durable rubber outsole.",
         "aspects": {"style": "classic", "durability": "good"}, "verified_purchase": True, "created_at": "2026-07-29"},
        {"author": "Suresh Gupta", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.10,
         "comment": "Good starter running shoe, but slightly heavy compared to Nike Revolution.",
         "aspects": {"weight": "slightly_heavy", "value": "fair"}, "verified_purchase": True, "created_at": "2026-07-21"},
        {"author": "Pooja Hegde", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.90,
         "comment": "Very comfortable arch support. Wore them all day at work without any fatigue.",
         "aspects": {"arch_support": "great", "comfort": "all_day"}, "verified_purchase": True, "created_at": "2026-07-16"},
        {"author": "Arun Prasad", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.72,
         "comment": "Decent grip on paved tracks. Tongue stays in place well.",
         "aspects": {"grip": "decent"}, "verified_purchase": True, "created_at": "2026-07-11"},
        {"author": "Divya Nambiar", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.55,
         "comment": "The heel cushioning feels too firm for marathon training. Best only for short gym sessions.",
         "aspects": {"firmness": "too_stiff", "versatility": "limited"}, "verified_purchase": True, "created_at": "2026-07-08"},
        {"author": "Gaurav Bansal", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.81,
         "comment": "Durable upper fabric. Survives muddy monsoon park runs without tearing.",
         "aspects": {"durability": "rugged", "build": "sturdy"}, "verified_purchase": True, "created_at": "2026-06-30"},
        {"author": "Simran Kaur", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.20,
         "comment": "Good fit, but laces are surprisingly long and need double knotting.",
         "aspects": {"laces": "too_long", "fit": "acceptable"}, "verified_purchase": False, "created_at": "2026-06-25"},
        {"author": "Karthik V", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.75,
         "comment": "Value for money at ₹2899. Cloudfoam midsole gives decent rebound.",
         "aspects": {"rebound": "good", "pricing": "fair"}, "verified_purchase": True, "created_at": "2026-06-19"},
        {"author": "Rahul Sethi", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.68,
         "comment": "After 4 weeks the heel inner lining started wearing off. Disappointed with internal stitch durability.",
         "aspects": {"lining": "worn_out", "quality": "subpar"}, "verified_purchase": True, "created_at": "2026-06-14"},
        {"author": "Swati Dave", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "Really lightweight and looks great with gym joggers. True to size UK 9.",
         "aspects": {"fit": "perfect", "look": "sleek"}, "verified_purchase": True, "created_at": "2026-06-08"},
    ],

    # -------------------------------------------------------------------------
    # 3. Puma Flyer Runner
    # -------------------------------------------------------------------------
    "Puma Flyer Runner": [
        {"author": "Abhishek Dubey", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.75,
         "comment": "Softfoam sockliner gives a cushy step-in feel immediately. Great daily beater.",
         "aspects": {"sockliner": "soft", "comfort": "high"}, "verified_purchase": True, "created_at": "2026-08-03"},
        {"author": "Ishaan Chawla", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.82,
         "comment": "Shadow Grey colorway looks minimal and premium. Very light on foot.",
         "aspects": {"color": "attractive", "weight": "featherlight"}, "verified_purchase": True, "created_at": "2026-07-27"},
        {"author": "Sunita Ghosh", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.08,
         "comment": "Fine for brisk walking and grocery runs, but sole is too flat for serious outdoor running.",
         "aspects": {"cushioning": "minimal", "activity": "walking_only"}, "verified_purchase": True, "created_at": "2026-07-20"},
        {"author": "Raghav Murthy", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.78,
         "comment": "Good grip on concrete. Heel collar is well cushioned against rubbing.",
         "aspects": {"grip": "good", "collar": "padded"}, "verified_purchase": True, "created_at": "2026-07-14"},
        {"author": "Pallavi Reddy", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "Extremely comfortable foam bed. My knees don't ache after 30 mins on treadmill.",
         "aspects": {"joint_comfort": "gentle", "midsole": "soft"}, "verified_purchase": True, "created_at": "2026-07-09"},
        {"author": "Naveen Tiwari", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.76,
         "comment": "Outsole rubber wore out near the ball of the foot in under two months. Lacks abrasion resistance.",
         "aspects": {"outsole": "worn_prematurely", "durability": "poor"}, "verified_purchase": True, "created_at": "2026-07-01"},
        {"author": "Shalini Mathur", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.71,
         "comment": "Affordable Puma trainers. Snug midfoot wrap keeps foot secure.",
         "aspects": {"lockdown": "snug", "value": "good"}, "verified_purchase": True, "created_at": "2026-06-26"},
        {"author": "Vikas Agarwal", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.12,
         "comment": "Sole squeaks a little on tiled office floors when walking fast.",
         "aspects": {"noise": "squeaky", "fit": "acceptable"}, "verified_purchase": False, "created_at": "2026-06-18"},
        {"author": "Bhavna Kapoor", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Breathable fabric and very flexible toe crease. Perfect for summer training.",
         "aspects": {"breathability": "excellent", "flexibility": "natural"}, "verified_purchase": True, "created_at": "2026-06-11"},
        {"author": "Varun Singhal", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.62,
         "comment": "Shoe profile is quite narrow. Had to return size 9 and size up to 10.",
         "aspects": {"sizing": "runs_small", "width": "tight"}, "verified_purchase": True, "created_at": "2026-06-04"},
    ],

    # -------------------------------------------------------------------------
    # 4. ASICS Gel Contend
    # -------------------------------------------------------------------------
    "ASICS Gel Contend": [
        {"author": "Dr. Prateek Pillai", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.96,
         "comment": "Superior rearfoot GEL technology. Unmatched shock absorption for runners with mild shin splints.",
         "aspects": {"gel_cushioning": "exceptional", "orthopedic": "recommended"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Anjali Sundaram", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "Best running shoes under ₹3000 hands down. Heel counter holds foot like a glove.",
         "aspects": {"heel_lock": "exceptional", "comfort": "top_tier"}, "verified_purchase": True, "created_at": "2026-07-31"},
        {"author": "Harshvardhan Rao", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "Amplifoam midsole provides a balanced ride that is neither too mushy nor rock hard.",
         "aspects": {"midsole": "balanced", "stability": "high"}, "verified_purchase": True, "created_at": "2026-07-25"},
        {"author": "Rohit Bhatt", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Excellent construction. Stitching along toe cap prevents premature blowouts.",
         "aspects": {"stitching": "reinforced", "durability": "high"}, "verified_purchase": True, "created_at": "2026-07-18"},
        {"author": "Gayatri Krishnan", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "True to size 8. Electric blue looks vibrant and sporty. Breathability is first class.",
         "aspects": {"color": "vibrant", "breathability": "excellent"}, "verified_purchase": True, "created_at": "2026-07-12"},
        {"author": "Sanjay Madan", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.77,
         "comment": "Very comfortable for 10K training. Solid rubber outsole bites asphalt securely.",
         "aspects": {"traction": "dependable", "long_distance": "suited"}, "verified_purchase": True, "created_at": "2026-07-07"},
        {"author": "Priyanka Saxena", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Ortholite sockliner provides dry moisture management. Zero blisters so far.",
         "aspects": {"insole": "ortholite", "anti_blister": "true"}, "verified_purchase": True, "created_at": "2026-06-28"},
        {"author": "Sameer Kulkarni", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.22,
         "comment": "Very comfortable shoe, though design looks a bit utilitarian compared to Nike.",
         "aspects": {"aesthetic": "traditional", "performance": "high"}, "verified_purchase": False, "created_at": "2026-06-21"},
        {"author": "Ritika Chopra", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.92,
         "comment": "High arch friendly. Gives continuous stability during uneven outdoor trail jogs.",
         "aspects": {"arch_support": "strong", "terrain": "versatile"}, "verified_purchase": True, "created_at": "2026-06-15"},
        {"author": "Kunal Bhasin", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.78,
         "comment": "Solid mid-tier runners. Worth every rupee at ₹2999.",
         "aspects": {"value": "worthwhile"}, "verified_purchase": True, "created_at": "2026-06-09"},
        {"author": "Mohit Soni", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.58,
         "comment": "Shoe is a bit heavy compared to superlight racing flats. A workhorse, not a speed shoe.",
         "aspects": {"weight": "heavy", "speed": "moderate"}, "verified_purchase": True, "created_at": "2026-06-02"},
    ],

    # -------------------------------------------------------------------------
    # 5. Reebok Energen Lite
    # -------------------------------------------------------------------------
    "Reebok Energen Lite": [
        {"author": "Aditya Sengupta", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.73,
         "comment": "Very light shoe for ₹2499. FuelFoam midsole gives a nice springy push on toes.",
         "aspects": {"weight": "ultra_light", "energy_return": "springy"}, "verified_purchase": True, "created_at": "2026-08-01"},
        {"author": "Pooja Malhotra", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.80,
         "comment": "Great everyday gym shoe. Vector Navy shade goes well with dark athletic tracksuits.",
         "aspects": {"color": "attractive", "gym_use": "ideal"}, "verified_purchase": True, "created_at": "2026-07-26"},
        {"author": "Tarun Kapoor", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.78,
         "comment": "Sole cushioning bottomed out after 6 weeks of 5K running. Felt hard ground impact.",
         "aspects": {"midsole": "deflated_quickly", "durability": "poor"}, "verified_purchase": True, "created_at": "2026-07-17"},
        {"author": "Meenakshi Das", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.02,
         "comment": "Okay for light treadmill walking, but lacks arch support for people with pronation.",
         "aspects": {"arch_support": "weak", "stability": "low"}, "verified_purchase": True, "created_at": "2026-07-12"},
        {"author": "Devendra Pal", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.65,
         "comment": "The heel rubber pad peeled off slightly at the corner. Glue quality could be better.",
         "aspects": {"glue": "weak", "outsole": "peeled"}, "verified_purchase": True, "created_at": "2026-07-06"},
        {"author": "Nitin Srivastava", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.70,
         "comment": "Mesh is breathable and dry. No sweaty feet issues in hot weather.",
         "aspects": {"breathability": "good"}, "verified_purchase": True, "created_at": "2026-06-29"},
        {"author": "Shruti Bakshi", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.18,
         "comment": "Fit is on the looser side. Might want to consider thick socks.",
         "aspects": {"sizing": "wide_fit"}, "verified_purchase": False, "created_at": "2026-06-23"},
        {"author": "Lalit Mehra", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.72,
         "comment": "Very decent price point for casual gym visitors.",
         "aspects": {"affordability": "high"}, "verified_purchase": True, "created_at": "2026-06-16"},
        {"author": "Preeti Sinha", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.74,
         "comment": "Insole slides backward inside the shoe when doing sprints. Had to glue it down.",
         "aspects": {"insole": "slipping", "build": "flawed"}, "verified_purchase": True, "created_at": "2026-06-07"},
        {"author": "Alok Ranjan", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.69,
         "comment": "Super lightweight kicks. Good budget shoe if your expectations are realistic.",
         "aspects": {"weight": "light", "price": "cheap"}, "verified_purchase": True, "created_at": "2026-05-31"},
    ],

    # -------------------------------------------------------------------------
    # 6. Nike Downshifter 12
    # -------------------------------------------------------------------------
    "Nike Downshifter 12": [
        {"author": "Karan Singhal", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.91,
         "comment": "Midfoot fit band really locks foot securely. Outstanding lockdown when taking sharp corners.",
         "aspects": {"lockdown": "superb", "stability": "high"}, "verified_purchase": True, "created_at": "2026-08-03"},
        {"author": "Vandana Rao", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Soft foam through the midsole delivers smooth transition from heel strike to toe off.",
         "aspects": {"transition": "smooth", "midsole": "soft"}, "verified_purchase": True, "created_at": "2026-07-29"},
        {"author": "Manoj Hegde", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Anthracite Black with Volt accents looks athletic and modern. Solid road grip.",
         "aspects": {"style": "sporty", "grip": "solid"}, "verified_purchase": True, "created_at": "2026-07-22"},
        {"author": "Deepika Bhatt", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "Upper mesh is lightweight yet structured. Great for 5K to 8K park runs.",
         "aspects": {"breathability": "good", "distance": "medium_range"}, "verified_purchase": True, "created_at": "2026-07-16"},
        {"author": "Ashish Bajaj", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.20,
         "comment": "Comfortable shoe overall, but toe tip bumper could use stronger rubber reinforcement.",
         "aspects": {"toe_protection": "moderate"}, "verified_purchase": True, "created_at": "2026-07-11"},
        {"author": "Geeta Raman", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Durable rubber outsole with flex grooves that bend naturally with every stride.",
         "aspects": {"flexibility": "natural", "outsole": "durable"}, "verified_purchase": True, "created_at": "2026-07-04"},
        {"author": "Saurabh Nanda", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.71,
         "comment": "Slight heel slip when running at faster pace. Had to use runner's loop lacing technique.",
         "aspects": {"heel_slip": "present", "lockdown": "imperfect"}, "verified_purchase": True, "created_at": "2026-06-27"},
        {"author": "Smita Varma", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.74,
         "comment": "Reliable Nike daily trainer under ₹2700. Good quality for price.",
         "aspects": {"value": "good", "brand": "trusted"}, "verified_purchase": True, "created_at": "2026-06-19"},
        {"author": "Naveen Goswami", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.05,
         "comment": "Adequate for beginners. Lacks bouncy energy return compared to Zoom models.",
         "aspects": {"responsiveness": "flat", "beginner": "friendly"}, "verified_purchase": False, "created_at": "2026-06-12"},
        {"author": "Chhavi Jain", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Very comfortable cushioning. Arrived within 2 days in perfect Nike packaging.",
         "aspects": {"cushioning": "plush", "shipping": "fast"}, "verified_purchase": True, "created_at": "2026-06-05"},
    ],

    # -------------------------------------------------------------------------
    # 7. Adidas Galaxy 7
    # -------------------------------------------------------------------------
    "Adidas Galaxy 7": [
        {"author": "Vinay Kulkarni", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.83,
         "comment": "Cloudfoam midsole provides immediate plushness. Walking 10,000 steps feels effortless.",
         "aspects": {"comfort": "high", "cushioning": "cloudfoam"}, "verified_purchase": True, "created_at": "2026-08-02"},
        {"author": "Rashmi Pillai", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.77,
         "comment": "Royal Blue color looks rich. Fabric has good ventilation and dries quickly.",
         "aspects": {"color": "rich", "ventilation": "good"}, "verified_purchase": True, "created_at": "2026-07-27"},
        {"author": "Pradeep Rawat", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.14,
         "comment": "Decent pair for ₹2599. Soles are a bit squeaky on smooth office marble.",
         "aspects": {"price": "budget", "noise": "squeaky"}, "verified_purchase": True, "created_at": "2026-07-19"},
        {"author": "Komal Shinde", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Very lightweight on feet. Tongue padding is soft against top of foot.",
         "aspects": {"weight": "light", "tongue": "padded"}, "verified_purchase": True, "created_at": "2026-07-13"},
        {"author": "Hemant Mishra", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.69,
         "comment": "Outer mesh tore near pinky toe seam after two months of regular running.",
         "aspects": {"durability": "poor", "seam": "torn"}, "verified_purchase": True, "created_at": "2026-07-06"},
        {"author": "Aishwarya Sen", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.75,
         "comment": "Good grip on concrete pavement. Reliable running companion.",
         "aspects": {"grip": "reliable"}, "verified_purchase": True, "created_at": "2026-06-29"},
        {"author": "Bharat Bhushan", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.22,
         "comment": "Good arch comfort but shoe width runs slightly narrow in toe section.",
         "aspects": {"width": "narrow", "arch": "adequate"}, "verified_purchase": False, "created_at": "2026-06-20"},
        {"author": "Tanya Agarwal", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "Super comfy! Wear them to college and gym every single day without complaints.",
         "aspects": {"versatility": "high", "comfort": "superb"}, "verified_purchase": True, "created_at": "2026-06-13"},
        {"author": "Girish Nair", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.72,
         "comment": "Solid everyday sneaker-runner combo for the price.",
         "aspects": {"versatility": "good"}, "verified_purchase": True, "created_at": "2026-06-06"},
        {"author": "Shikha Malhotra", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.61,
         "comment": "Heel drop feels higher than advertised. Caused mild knee fatigue on longer runs.",
         "aspects": {"heel_drop": "high", "fatigue": "noticeable"}, "verified_purchase": True, "created_at": "2026-05-30"},
    ],

    # -------------------------------------------------------------------------
    # 8. Puma Softride Enzo
    # -------------------------------------------------------------------------
    "Puma Softride Enzo": [
        {"author": "Kartik Natarajan", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "The Softride EVA compound is like walking on marshmallows. Unbeatable all-day plushness.",
         "aspects": {"cushioning": "cloud_like", "comfort": "exceptional"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Bhavya Trivedi", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Clam-shell slip-on construction with exaggerated collar makes them super easy to slide into.",
         "aspects": {"entry": "slip_on", "collar": "plush"}, "verified_purchase": True, "created_at": "2026-07-30"},
        {"author": "Rishi Saxena", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.78,
         "comment": "High Rise Grey with Neon Lime looks futuristic and eye-catching in the gym.",
         "aspects": {"design": "futuristic", "color": "neon_pop"}, "verified_purchase": True, "created_at": "2026-07-24"},
        {"author": "Nandini Ghosh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "TPU midfoot cage locks the foot in securely during lateral side shuffles.",
         "aspects": {"lateral_stability": "high", "cage": "supportive"}, "verified_purchase": True, "created_at": "2026-07-17"},
        {"author": "Vivek Somani", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.08,
         "comment": "Awesome for casual wear, but foam is too squishy for heavy barbell squats.",
         "aspects": {"stability_squats": "low", "casual_comfort": "high"}, "verified_purchase": True, "created_at": "2026-07-10"},
        {"author": "Pallavi Deshmukh", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.92,
         "comment": "SoftFoam+ insole gives extra cushioning at heel strike. Zero foot fatigue after standing shifts.",
         "aspects": {"heel_cushion": "soft", "standing": "painless"}, "verified_purchase": True, "created_at": "2026-07-03"},
        {"author": "Ashok Reddy", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.73,
         "comment": "The high heel pull tab rubs against Achilles tendon without high socks.",
         "aspects": {"heel_rub": "annoying", "socks": "crew_required"}, "verified_purchase": True, "created_at": "2026-06-25"},
        {"author": "Kavita Seth", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.76,
         "comment": "Great road grip and modern streetstyle silhouette. Excellent ₹2999 value.",
         "aspects": {"aesthetic": "modern", "grip": "good"}, "verified_purchase": True, "created_at": "2026-06-17"},
        {"author": "Jayesh Parekh", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.16,
         "comment": "Comfortable, but fit is snug around the instep. Wide feet buyers beware.",
         "aspects": {"instep": "tight", "width": "snug"}, "verified_purchase": False, "created_at": "2026-06-10"},
        {"author": "Madhavi Iyer", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.90,
         "comment": "My favorite sneakers for cardio and walking. Super soft and lightweight.",
         "aspects": {"comfort": "top_rated"}, "verified_purchase": True, "created_at": "2026-06-03"},
    ],

    # -------------------------------------------------------------------------
    # 9. Skechers Go Run
    # -------------------------------------------------------------------------
    "Skechers Go Run": [
        {"author": "Suresh Chandra", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Hyper Burst / Ultra Flight foam feels like floating. Greatest walking comfort on the market.",
         "aspects": {"cushioning": "supreme", "impact_protection": "excellent"}, "verified_purchase": True, "created_at": "2026-08-02"},
        {"author": "Lata Venkatesh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Goga Mat air-cooled insole provides high rebound cushioning. Feet stay fresh all day.",
         "aspects": {"insole": "goga_mat", "ventilation": "cool"}, "verified_purchase": True, "created_at": "2026-07-28"},
        {"author": "Dhananjay Roy", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Machine washable design makes cleaning super convenient. Charcoal Black color hides dust well.",
         "aspects": {"washable": "convenient", "maintenance": "easy"}, "verified_purchase": True, "created_at": "2026-07-21"},
        {"author": "Preeti Talwar", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Midfoot strike zone promotes efficient running posture. Very pleasant ride.",
         "aspects": {"running_form": "midfoot_strike", "ride": "smooth"}, "verified_purchase": True, "created_at": "2026-07-15"},
        {"author": "Naveen Kaushik", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.10,
         "comment": "Good comfort, but outsole rubber traction pads wear thin on coarse gravel tracks.",
         "aspects": {"traction_wear": "fast_on_gravel"}, "verified_purchase": True, "created_at": "2026-07-08"},
        {"author": "Sunil Nair", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Toe box has plenty of room for natural toe splay. No chafing or cramped toes.",
         "aspects": {"toe_box": "generous", "comfort": "unrestricted"}, "verified_purchase": True, "created_at": "2026-06-30"},
        {"author": "Archana Verma", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.60,
         "comment": "A bit loose in the heel cup. Foot tends to slide forward on steep downward slopes.",
         "aspects": {"heel_security": "loose", "downhill": "unstable"}, "verified_purchase": True, "created_at": "2026-06-22"},
        {"author": "Pradeep Chari", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.76,
         "comment": "Great for recovery jogs after hard leg days. Very gentle on ankle joints.",
         "aspects": {"recovery": "gentle", "joints": "low_stress"}, "verified_purchase": True, "created_at": "2026-06-15"},
        {"author": "Shweta Menon", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.15,
         "comment": "Comfortable but looks more like an orthopedic sneaker than a trendy shoe.",
         "aspects": {"aesthetic": "practical", "comfort": "high"}, "verified_purchase": False, "created_at": "2026-06-07"},
        {"author": "Gaurav Kohli", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "Featherlight weight. You barely feel them on your feet during long jogs.",
         "aspects": {"weight": "ultralight"}, "verified_purchase": True, "created_at": "2026-05-31"},
    ],

    # -------------------------------------------------------------------------
    # 10. New Balance Fresh Foam
    # -------------------------------------------------------------------------
    "New Balance Fresh Foam": [
        {"author": "Aditi Ramachandran", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.95,
         "comment": "Precision-engineered Fresh Foam midsole is heaven for long-distance training. Phenomenal shock damping.",
         "aspects": {"fresh_foam": "elite", "comfort": "top_notch"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Rajat Singhania", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.92,
         "comment": "Eclipse Blue with Silver accents is stunning in person. Excellent build quality and stitching.",
         "aspects": {"styling": "gorgeous", "build": "flawless"}, "verified_purchase": True, "created_at": "2026-07-31"},
        {"author": "Mukul Grover", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Wide, supportive base delivers confidence on uneven sidewalks and asphalt bends.",
         "aspects": {"base": "wide_stable", "stability": "high"}, "verified_purchase": True, "created_at": "2026-07-26"},
        {"author": "Snehal Kadam", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Engineered mesh upper breathes nicely without letting road dust enter.",
         "aspects": {"mesh": "breathable_dense", "dust_protection": "good"}, "verified_purchase": True, "created_at": "2026-07-20"},
        {"author": "Kishore Pillai", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Great heel collar foam hug. Keeps heel securely planted without friction.",
         "aspects": {"heel_hug": "plush"}, "verified_purchase": True, "created_at": "2026-07-14"},
        {"author": "Tanvi Kapoor", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.20,
         "comment": "Very comfortable shoe, though price is slightly higher at ₹3299. Worth it if you run daily.",
         "aspects": {"price": "premium", "worth": "fair"}, "verified_purchase": True, "created_at": "2026-07-07"},
        {"author": "Vikas Mathur", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Blown rubber outsole has held up nicely over 150km. Great traction on tarmac.",
         "aspects": {"outsole": "blown_rubber", "grip": "excellent"}, "verified_purchase": True, "created_at": "2026-06-29"},
        {"author": "Bhavik Jain", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.55,
         "comment": "Arch support is a bit aggressive if you have extremely flat feet. Needs getting used to.",
         "aspects": {"arch": "firm", "flat_feet": "adjustment_needed"}, "verified_purchase": True, "created_at": "2026-06-21"},
        {"author": "Pooja Vashisht", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Zero knee aches during 10K runs. New Balance really nailed the geometry here.",
         "aspects": {"geometry": "smooth_rocker", "knee_relief": "proven"}, "verified_purchase": True, "created_at": "2026-06-14"},
        {"author": "Amit Trivedi", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.80,
         "comment": "Comfortable, premium feel throughout. Fits true to size UK 9.",
         "aspects": {"sizing": "accurate", "feel": "premium"}, "verified_purchase": True, "created_at": "2026-06-07"},
    ],

    # -------------------------------------------------------------------------
    # 11. Nike Revolution 7
    # -------------------------------------------------------------------------
    "Nike Revolution 7": [
        {"author": "Siddharth Nambiar", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "Significant upgrade over the Revolution 6! Softer foam and much roomier forefoot.",
         "aspects": {"upgrade": "huge_improvement", "forefoot": "roomier"}, "verified_purchase": True, "created_at": "2026-08-03"},
        {"author": "Kavita Nair", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.91,
         "comment": "Triple White look is pristine and matches any outfit. Soft touchpoints at heel collar.",
         "aspects": {"style": "clean_triple_white", "collar": "soft"}, "verified_purchase": True, "created_at": "2026-07-29"},
        {"author": "Umesh Patel", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Generative traction pattern on outsole gives confident grip on road and wet tiles.",
         "aspects": {"traction": "generative_pattern", "grip": "reliable"}, "verified_purchase": True, "created_at": "2026-07-23"},
        {"author": "Ananya Ghosh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Lightweight and springy. The foam midsole absorbs footsteps very quietly.",
         "aspects": {"quiet": "soft_landing", "responsiveness": "good"}, "verified_purchase": True, "created_at": "2026-07-17"},
        {"author": "Naveen Bhatt", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.78,
         "comment": "True to size UK 10. Feels snug without creating hot spots.",
         "aspects": {"fit": "true_to_size", "no_hotspots": "verified"}, "verified_purchase": True, "created_at": "2026-07-11"},
        {"author": "Pooja Deshpande", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.18,
         "comment": "White version gets dusty easily on outdoor roads. Need to wash it regularly.",
         "aspects": {"color_maintenance": "dust_prone"}, "verified_purchase": True, "created_at": "2026-07-04"},
        {"author": "Rohit Verma", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Ran 8 km in these right out of the box with zero blisters. Best Nike value runner.",
         "aspects": {"break_in": "none_needed", "comfort": "instant"}, "verified_purchase": True, "created_at": "2026-06-26"},
        {"author": "Shalini Dixit", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.76,
         "comment": "Good flexible sole. Great for daily treadmill and strength workouts.",
         "aspects": {"flexibility": "good", "versatility": "cross_training"}, "verified_purchase": False, "created_at": "2026-06-18"},
        {"author": "Harish Menon", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.59,
         "comment": "Insole could have more arch contouring. I swapped in my own custom orthotic.",
         "aspects": {"arch_support": "flat_insole"}, "verified_purchase": True, "created_at": "2026-06-10"},
        {"author": "Divya Sharma", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Super stylish and cushioned. Very happy with the purchase.",
         "aspects": {"overall": "highly_recommended"}, "verified_purchase": True, "created_at": "2026-06-02"},
    ],

    # -------------------------------------------------------------------------
    # 12. Adidas Duramo SL
    # -------------------------------------------------------------------------
    "Adidas Duramo SL": [
        {"author": "Sachin Tendulkar", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Lightmotion cushioning gives a quick, responsive toe-off. Great tempo trainer.",
         "aspects": {"cushioning": "lightmotion", "tempo": "responsive"}, "verified_purchase": True, "created_at": "2026-08-01"},
        {"author": "Meena Agarwal", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Mesh upper is very light and breathable. Keeps feet cool in Chennai heat.",
         "aspects": {"breathability": "excellent", "cooling": "effective"}, "verified_purchase": True, "created_at": "2026-07-27"},
        {"author": "Girish Prabhu", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.83,
         "comment": "Adiwear outsole rubber is exceptionally tough. Minimal wear after 200 km.",
         "aspects": {"adiwear": "indestructible", "durability": "high"}, "verified_purchase": True, "created_at": "2026-07-21"},
        {"author": "Sunita Rao", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.10,
         "comment": "Good shoe, but slightly stiff midfoot for the first week until broken in.",
         "aspects": {"midfoot": "stiff_initially", "break_in": "1_week"}, "verified_purchase": True, "created_at": "2026-07-14"},
        {"author": "Pankaj Vats", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.74,
         "comment": "Core Black with Silver Metallic stripes looks sharp in the gym.",
         "aspects": {"styling": "sleek"}, "verified_purchase": True, "created_at": "2026-07-08"},
        {"author": "Rani Mukherjee", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.90,
         "comment": "Fits like a dream. Soft heel padding prevents any chafing on Achilles.",
         "aspects": {"fit": "perfect", "achilles_comfort": "gentle"}, "verified_purchase": True, "created_at": "2026-06-30"},
        {"author": "Ashwin Balaji", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.72,
         "comment": "The shoe tongue slips to the side constantly while running. No lace-loop on the tongue.",
         "aspects": {"tongue_slip": "annoying", "design_flaw": "no_lace_loop"}, "verified_purchase": True, "created_at": "2026-06-22"},
        {"author": "Neeta Kulkarni", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "Super light and supportive. Outstanding price-to-performance ratio.",
         "aspects": {"performance": "high", "weight": "light"}, "verified_purchase": True, "created_at": "2026-06-15"},
        {"author": "Arunabh Kumar", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.17,
         "comment": "Decent daily trainer. Foam is a bit firm compared to Cloudfoam models.",
         "aspects": {"firmness": "medium_firm"}, "verified_purchase": False, "created_at": "2026-06-08"},
        {"author": "Deepa Sundar", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Very comfortable for morning jogging and fitness classes.",
         "aspects": {"jogging": "comfortable"}, "verified_purchase": True, "created_at": "2026-06-01"},
    ],

    # -------------------------------------------------------------------------
    # 13. Puma Velocity Nitro
    # -------------------------------------------------------------------------
    "Puma Velocity Nitro": [
        {"author": "Varun Grover", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.97,
         "comment": "NITRO FOAM is a game changer! Incredible bounce, explosive energy return and ultra plush cushioning.",
         "aspects": {"nitro_foam": "elite_rebound", "cushioning": "top_tier"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Shreya Ghoshal", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.95,
         "comment": "PUMAGRIP outsole is the grippiest rubber in the running shoe industry. Sticks to wet roads like glue.",
         "aspects": {"pumagrip": "industry_best", "traction": "unreal"}, "verified_purchase": True, "created_at": "2026-07-30"},
        {"author": "Abhay Deol", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.90,
         "comment": "Neon Orange colorway looks blazing fast. Ran a half marathon personal record in these.",
         "aspects": {"racing": "half_marathon_ready", "style": "fast"}, "verified_purchase": True, "created_at": "2026-07-25"},
        {"author": "Tanvi Azmi", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "Engineered mesh fits securely around midfoot without pinching. Breathability is 10/10.",
         "aspects": {"midfoot_wrap": "snug", "breathability": "maximum"}, "verified_purchase": True, "created_at": "2026-07-19"},
        {"author": "Karthik Raja", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.82,
         "comment": "Very smooth heel-to-toe transition. Responsive enough for sprint intervals.",
         "aspects": {"intervals": "fast", "transitions": "seamless"}, "verified_purchase": True, "created_at": "2026-07-12"},
        {"author": "Ragini Khanna", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "Worth every bit of ₹3499. Beats shoes that cost twice as much.",
         "aspects": {"value": "exceptional_flagship"}, "verified_purchase": True, "created_at": "2026-07-05"},
        {"author": "Manish Paul", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.20,
         "comment": "Fantastic shoe, but heel collar padding is slightly thin compared to Brooks.",
         "aspects": {"heel_collar": "minimal"}, "verified_purchase": False, "created_at": "2026-06-27"},
        {"author": "Geetanjali Thapa", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Lightweight, cushioned, and ridiculously fast. My daily mileage shoe now.",
         "aspects": {"daily_mileage": "perfect_choice"}, "verified_purchase": True, "created_at": "2026-06-19"},
        {"author": "Sameer Nair", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.55,
         "comment": "Runs half a size small. Recommend going up a size if you have wide toes.",
         "aspects": {"sizing": "half_size_small"}, "verified_purchase": True, "created_at": "2026-06-11"},
        {"author": "Anupam Roy", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Nitro foam hasn't lost any bounciness even after 300 km of road training.",
         "aspects": {"resilience": "durable_bounce"}, "verified_purchase": True, "created_at": "2026-06-03"},
    ],

    # -------------------------------------------------------------------------
    # 14. ASICS Gel Excite
    # -------------------------------------------------------------------------
    "ASICS Gel Excite": [
        {"author": "Naveen Jindal", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.92,
         "comment": "Rearfoot GEL paired with Amplifoam Plus gives a luxurious soft landing. Excellent knee protection.",
         "aspects": {"gel_cushion": "soft", "knee_care": "great"}, "verified_purchase": True, "created_at": "2026-08-02"},
        {"author": "Pratibha Patil", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Jacquard mesh upper has great multidirectional stretch. Hugs foot naturally.",
         "aspects": {"mesh": "jacquard_stretch", "fit": "adaptive"}, "verified_purchase": True, "created_at": "2026-07-28"},
        {"author": "Tushar Deshmukh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Island Blue color scheme is eye-catching and sporty. Solid outsole traction.",
         "aspects": {"color": "attractive", "traction": "dependable"}, "verified_purchase": True, "created_at": "2026-07-22"},
        {"author": "Radhika Merchant", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Very comfortable arch support. Wore them on a walking tour with zero discomfort.",
         "aspects": {"walking": "all_day", "arch": "supportive"}, "verified_purchase": True, "created_at": "2026-07-16"},
        {"author": "Dinesh Karthik", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.08,
         "comment": "Good comfort, but shoe weight is slightly higher than Nike Downshifter.",
         "aspects": {"weight": "moderate"}, "verified_purchase": True, "created_at": "2026-07-09"},
        {"author": "Seema Biswas", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.91,
         "comment": "Ortholite insole keeps feet odor-free and cushioned. Highly satisfied at ₹2899.",
         "aspects": {"insole": "ortholite", "anti_odor": "verified"}, "verified_purchase": True, "created_at": "2026-07-02"},
        {"author": "Mukesh Ambani", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "Solid heel lockdown and padded collar prevent any blister formation.",
         "aspects": {"heel_lock": "secure", "comfort": "high"}, "verified_purchase": True, "created_at": "2026-06-25"},
        {"author": "Ila Arun", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.16,
         "comment": "Good running shoe for paved roads, but mud sticks in the outsole flex grooves.",
         "aspects": {"mud_retention": "high_grooves"}, "verified_purchase": False, "created_at": "2026-06-17"},
        {"author": "Vijay Shekhar", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.57,
         "comment": "Cushioning is slightly firm in the forefoot. Great heel gel, but forefoot needs more foam.",
         "aspects": {"forefoot_cushion": "firm"}, "verified_purchase": True, "created_at": "2026-06-09"},
        {"author": "Smriti Irani", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Durable, stable and very comfortable. ASICS quality is always consistent.",
         "aspects": {"durability": "high", "stability": "rock_solid"}, "verified_purchase": True, "created_at": "2026-06-02"},
    ],

    # -------------------------------------------------------------------------
    # 15. Reebok Floatride
    # -------------------------------------------------------------------------
    "Reebok Floatride": [
        {"author": "Chetan Bhagat", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Floatride Energy Foam is one of the best value foams around. Bouncy and responsive.",
         "aspects": {"energy_foam": "responsive", "bounce": "great"}, "verified_purchase": True, "created_at": "2026-08-01"},
        {"author": "Twinkle Khanna", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Super clean Black Cyan design. Incredibly lightweight and agile on tarmac.",
         "aspects": {"style": "sleek", "weight": "light"}, "verified_purchase": True, "created_at": "2026-07-27"},
        {"author": "Anupam Kher", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.77,
         "comment": "Full rubber outsole provides full contact grip without slippage.",
         "aspects": {"grip": "full_rubber"}, "verified_purchase": True, "created_at": "2026-07-20"},
        {"author": "Karisma Kapoor", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.91,
         "comment": "Ran a brisk 10K and felt practically zero leg fatigue. Excellent cushioning balance.",
         "aspects": {"mileage": "10k_approved", "damping": "superior"}, "verified_purchase": True, "created_at": "2026-07-14"},
        {"author": "Naseeruddin Shah", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.09,
         "comment": "Heel counter is relatively flexible. Might not suit severe overpronators.",
         "aspects": {"stability": "neutral_only"}, "verified_purchase": True, "created_at": "2026-07-07"},
        {"author": "Tabu Hashmi", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "Engineered mesh is durable and well ventilated. Fits true to size UK 9.",
         "aspects": {"fit": "true_to_size", "ventilation": "high"}, "verified_purchase": True, "created_at": "2026-06-29"},
        {"author": "Boman Irani", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.76,
         "comment": "Great road trainer at ₹2699. Performs far better than Energen Lite.",
         "aspects": {"value": "high"}, "verified_purchase": True, "created_at": "2026-06-21"},
        {"author": "Konkona Sen", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.15,
         "comment": "Laces are slightly slippery. Double knotting is required for long runs.",
         "aspects": {"laces": "slippery"}, "verified_purchase": False, "created_at": "2026-06-13"},
        {"author": "Paresh Rawal", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.70,
         "comment": "Insole fabric started fraying at the heel edge after 3 weeks of daily use.",
         "aspects": {"insole_fabric": "frayed"}, "verified_purchase": True, "created_at": "2026-06-05"},
        {"author": "Shabana Azmi", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Comfortable step-in feel and smooth stride cadence. Highly satisfied.",
         "aspects": {"stride": "smooth", "comfort": "high"}, "verified_purchase": True, "created_at": "2026-05-29"},
    ],

    # -------------------------------------------------------------------------
    # 16. Nike Air Zoom Pegasus 40
    # -------------------------------------------------------------------------
    "Nike Air Zoom Pegasus 40": [
        {"author": "Milind Soman", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.98,
         "comment": "The gold standard daily trainer. Dual Zoom Air units + React foam provide unmatched propulsive energy.",
         "aspects": {"zoom_air": "flawless", "react_foam": "magic", "cushioning": "legendary"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Ankita Konwar", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.96,
         "comment": "Single layer engineered mesh wraps the foot perfectly. Zero pressure on sensitive arch zones.",
         "aspects": {"upper": "custom_like_fit", "breathability": "top"}, "verified_purchase": True, "created_at": "2026-07-31"},
        {"author": "Abhinav Bindra", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "Waffle inspired outsole offers incredible traction on asphalt, wet track, and park gravel.",
         "aspects": {"traction": "waffle_grip", "versatility": "all_terrain"}, "verified_purchase": True, "created_at": "2026-07-26"},
        {"author": "P.V. Sindhu", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.90,
         "comment": "Laser Blue colorway looks fast even standing still. Superb heel lock prevents any slipping.",
         "aspects": {"heel_lock": "rock_solid", "design": "iconic"}, "verified_purchase": True, "created_at": "2026-07-20"},
        {"author": "Neeraj Chopra", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.95,
         "comment": "Survived 400+ km of intense cross-training and road miles. Outsole barely shows wear.",
         "aspects": {"durability": "phenomenal", "reactivity": "resilient"}, "verified_purchase": True, "created_at": "2026-07-14"},
        {"author": "Mary Kom", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "Plush collar padding and tongue eliminate lace bite completely.",
         "aspects": {"lace_bite": "eliminated", "collar": "plush"}, "verified_purchase": True, "created_at": "2026-07-08"},
        {"author": "Sunil Chhetri", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Smooth transition from foot strike to takeoff. Ideal for recovery runs and tempo paces alike.",
         "aspects": {"versatility": "daily_to_tempo"}, "verified_purchase": True, "created_at": "2026-07-01"},
        {"author": "Saina Nehwal", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.22,
         "comment": "A bit pricey at ₹3899, but you get what you pay for in durability and comfort.",
         "aspects": {"price": "premium", "quality": "matching"}, "verified_purchase": True, "created_at": "2026-06-23"},
        {"author": "Leander Paes", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Roomier toe box than Pegasus 39. Absolute workhorse for serious runners.",
         "aspects": {"toe_box": "improved"}, "verified_purchase": False, "created_at": "2026-06-15"},
        {"author": "Deepa Malik", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.81,
         "comment": "Excellent cushioning, though slightly warm during mid-afternoon summer runs.",
         "aspects": {"warmth": "slightly_warm"}, "verified_purchase": True, "created_at": "2026-06-07"},
    ],

    # -------------------------------------------------------------------------
    # 17. Under Armour HOVR Sonic 6
    # -------------------------------------------------------------------------
    "Under Armour HOVR Sonic 6": [
        {"author": "Vidyut Jammwal", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "UA HOVR technology eliminates impact and returns energy into every stride. Great gym cross-trainer.",
         "aspects": {"hovr_cushion": "zero_gravity", "energy_return": "high"}, "verified_purchase": True, "created_at": "2026-08-03"},
        {"author": "Tiger Shroff", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "External TPU heel counter delivers incredible structural support during sprints and plyometrics.",
         "aspects": {"heel_counter": "tpu_support", "stability": "rigid"}, "verified_purchase": True, "created_at": "2026-07-29"},
        {"author": "John Abraham", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Engineered spacer mesh upper with seamless design is lightweight and super breathable.",
         "aspects": {"upper": "seamless", "breathability": "ventilated"}, "verified_purchase": True, "created_at": "2026-07-24"},
        {"author": "Disha Patani", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.80,
         "comment": "Jet Black colorway looks aggressive and sleek with gym compression gear.",
         "aspects": {"aesthetic": "athletic_sleek"}, "verified_purchase": True, "created_at": "2026-07-18"},
        {"author": "Hrithik Roshan", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Blown rubber under forefoot gives high-abrasion durability. Very solid build.",
         "aspects": {"durability": "high", "traction": "confident"}, "verified_purchase": True, "created_at": "2026-07-12"},
        {"author": "Ranveer Singh", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.12,
         "comment": "Very firm ride compared to Nike Pegasus. Great for lifting weights, firm for marathon running.",
         "aspects": {"ride": "firm", "weightlifting": "good"}, "verified_purchase": True, "created_at": "2026-07-05"},
        {"author": "Shahid Kapoor", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.77,
         "comment": "Molded EVA sockliner provides extra resilience and step-in comfort.",
         "aspects": {"insole": "molded_eva"}, "verified_purchase": True, "created_at": "2026-06-27"},
        {"author": "Farhan Akhtar", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.58,
         "comment": "Narrow midfoot fit. Caused slight arch cramping on the first few runs.",
         "aspects": {"midfoot": "tight", "arch": "stiff"}, "verified_purchase": True, "created_at": "2026-06-19"},
        {"author": "Ayushmann Khurrana", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "High quality materials throughout. Under Armour build quality doesn't disappoint.",
         "aspects": {"quality": "premium"}, "verified_purchase": False, "created_at": "2026-06-11"},
        {"author": "Rajkummar Rao", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.75,
         "comment": "Reliable and durable athletic footwear for daily fitness enthusiasts.",
         "aspects": {"fitness": "dependable"}, "verified_purchase": True, "created_at": "2026-06-03"},
    ],

    # -------------------------------------------------------------------------
    # 18. Sony WH-CH520 Wireless Bluetooth Headphones
    # -------------------------------------------------------------------------
    "Sony WH-CH520 Wireless Bluetooth Headphones": [
        {"author": "A.R. Rahman", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.98,
         "comment": "Stellar 50-hour battery life! Charged once and listened for nearly two full weeks. DSEE audio upscaling brings compressed tracks alive.",
         "aspects": {"battery": "50_hours_monstrous", "sound_quality": "dsee_upscaling"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Shankar Mahadevan", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.95,
         "comment": "Multipoint connection switches effortlessly between my laptop Zoom calls and iPhone calls.",
         "aspects": {"multipoint": "flawless", "mic_quality": "clear"}, "verified_purchase": True, "created_at": "2026-07-31"},
        {"author": "Sonu Nigam", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.91,
         "comment": "Super lightweight on-ear design with plush memory foam cushions. Zero ear fatigue after 4-hour editing sessions.",
         "aspects": {"comfort": "featherlight", "ear_cups": "plush"}, "verified_purchase": True, "created_at": "2026-07-26"},
        {"author": "Sunidhi Chauhan", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "Sony Headphones Connect app has a custom 5-band EQ. Bass boost profile hits with punchy, clean bass.",
         "aspects": {"app_eq": "customizable", "bass": "tight_punchy"}, "verified_purchase": True, "created_at": "2026-07-21"},
        {"author": "Vishal Dadlani", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Matte Black finish is fingerprint resistant. Solid tactile volume and track buttons.",
         "aspects": {"build": "clean_matte", "controls": "tactile_buttons"}, "verified_purchase": True, "created_at": "2026-07-15"},
        {"author": "Shekhar Ravjiani", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.80,
         "comment": "Fast 3-minute quick charge delivers 1.5 hours of playback. Lifesaver before flights.",
         "aspects": {"quick_charge": "rapid"}, "verified_purchase": True, "created_at": "2026-07-09"},
        {"author": "Neha Kakkar", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Built-in microphone with beamforming suppresses background room echo nicely during office meetings.",
         "aspects": {"calls": "crystal_clear", "noise_reduction": "effective"}, "verified_purchase": True, "created_at": "2026-07-02"},
        {"author": "Badshah", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.22,
         "comment": "No Active Noise Cancellation, but passive on-ear isolation blocks moderate cafe chatter.",
         "aspects": {"anc": "passive_only", "isolation": "moderate"}, "verified_purchase": False, "created_at": "2026-06-24"},
        {"author": "Guru Randhawa", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Unbelievable value at ₹2999. Easily beats headphones priced at ₹5000+.",
         "aspects": {"value": "best_in_class"}, "verified_purchase": True, "created_at": "2026-06-16"},
        {"author": "Armaan Malik", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Headband has good flex without excessive clamping force on glasses frames.",
         "aspects": {"clamping_force": "gentle", "glasses_friendly": "yes"}, "verified_purchase": True, "created_at": "2026-06-08"},
        {"author": "Jubin Nautiyal", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.05,
         "comment": "Earcups swivel flat but do not fold inwards. Wish it included a soft pouch.",
         "aspects": {"portability": "swivel_only", "pouch": "missing"}, "verified_purchase": True, "created_at": "2026-05-31"},
    ],

    # -------------------------------------------------------------------------
    # 19. boAt Airdopes 141 ANC True Wireless
    # -------------------------------------------------------------------------
    "boAt Airdopes 141 ANC True Wireless": [
        {"author": "Kunal Kamra", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "Up to 32dB Active Noise Cancellation at just ₹1699 is insane value! Drowns out bus engine rumbling.",
         "aspects": {"anc": "32db_effective", "price": "dirt_cheap"}, "verified_purchase": True, "created_at": "2026-08-03"},
        {"author": "Zakir Khan", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.78,
         "comment": "Signature boAt thumping bass. Bollywood and hip hop tracks sound loud and vibrant.",
         "aspects": {"bass": "thumping_heavy", "volume": "loud"}, "verified_purchase": True, "created_at": "2026-07-29"},
        {"author": "Biswa Kalyan Rath", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.12,
         "comment": "Decent earbuds, but slight latency when playing fast paced shooters like BGMI.",
         "aspects": {"gaming_latency": "slight_delay"}, "verified_purchase": True, "created_at": "2026-07-23"},
        {"author": "Kenny Sebastian", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Battery lasts 42 hours total with the compact charging case. Type-C ASAP charge works well.",
         "aspects": {"battery": "42h_total", "case": "pocketable"}, "verified_purchase": True, "created_at": "2026-07-17"},
        {"author": "Anubhav Singh Bassi", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.74,
         "comment": "Microphone in windy conditions struggles. Caller complained about gust noise.",
         "aspects": {"wind_noise": "poor_mic", "outdoor_calls": "struggles"}, "verified_purchase": True, "created_at": "2026-07-10"},
        {"author": "Varun Thakur", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.74,
         "comment": "IPX5 water resistance survived heavy gym sweat and sudden drizzling rain.",
         "aspects": {"waterproof": "ipx5_sweatproof"}, "verified_purchase": True, "created_at": "2026-07-03"},
        {"author": "Aakash Gupta", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.62,
         "comment": "Touch controls are overly sensitive. Accidentally paused playback while adjusting ear tip.",
         "aspects": {"touch_sensors": "too_sensitive"}, "verified_purchase": True, "created_at": "2026-06-25"},
        {"author": "Rahul Subramanian", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.82,
         "comment": "Comfortable silicone ear tips in three sizes. Doesn't fall out during jogs.",
         "aspects": {"fit": "secure_jogging"}, "verified_purchase": False, "created_at": "2026-06-17"},
        {"author": "Urooj Ashfaq", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.76,
         "comment": "Emerald green color case looks stylish and youthful. Good purchase.",
         "aspects": {"color": "attractive"}, "verified_purchase": True, "created_at": "2026-06-09"},
        {"author": "Abhishek Upmanyu", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.08,
         "comment": "Sound is V-shaped with recessed mids. Good for rap, average for acoustic guitar.",
         "aspects": {"mids": "recessed", "tuning": "v_shaped"}, "verified_purchase": True, "created_at": "2026-06-01"},
    ],

    # -------------------------------------------------------------------------
    # 20. JBL Tune 510BT Pure Bass On-Ear
    # -------------------------------------------------------------------------
    "JBL Tune 510BT Pure Bass On-Ear": [
        {"author": "Kapil Sharma", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "JBL Pure Bass Sound delivers deep, satisfying sub-bass without distorting at maximum volume.",
         "aspects": {"sub_bass": "legendary", "distortion": "none"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Archana Puran Singh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Foldable design fits easily into gym bags. Bluetooth 5.0 connection is rock solid.",
         "aspects": {"foldable": "compact", "bluetooth": "stable"}, "verified_purchase": True, "created_at": "2026-07-30"},
        {"author": "Krushna Abhishek", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Up to 40 hours battery life. Quick 5-minute charge gives 2 hours of juice.",
         "aspects": {"battery": "40_hours", "fast_charge": "convenient"}, "verified_purchase": True, "created_at": "2026-07-24"},
        {"author": "Kiku Sharda", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Multi-point connection allows effortless toggling between tablet movies and phone.",
         "aspects": {"multipoint": "useful"}, "verified_purchase": True, "created_at": "2026-07-18"},
        {"author": "Sumona Chakravarti", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.10,
         "comment": "Clamping force is on the firmer side. Ears get warm after 2 continuous hours.",
         "aspects": {"clamping": "tight", "ear_warmth": "present"}, "verified_purchase": True, "created_at": "2026-07-11"},
        {"author": "Ali Asgar", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Siri and Google Assistant integration works instantly with single button press.",
         "aspects": {"voice_assistant": "seamless"}, "verified_purchase": True, "created_at": "2026-07-04"},
        {"author": "Sunil Grover", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.63,
         "comment": "Headband has minimal foam padding on top. Felt slight pressure on crown of head.",
         "aspects": {"headband": "underpadded"}, "verified_purchase": True, "created_at": "2026-06-26"},
        {"author": "Bharti Singh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "Deep Blue color is gorgeous. Sound clarity on vocals is crisp.",
         "aspects": {"color": "deep_blue", "vocals": "clear"}, "verified_purchase": False, "created_at": "2026-06-18"},
        {"author": "Harsh Limbachiyaa", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.75,
         "comment": "Sturdy hinges that don't rattle when walking. Great build for ₹2499.",
         "aspects": {"hinges": "sturdy", "durability": "solid"}, "verified_purchase": True, "created_at": "2026-06-10"},
        {"author": "Chandan Prabhakar", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.18,
         "comment": "Good headphones, mic is fine indoors but picks up street ambient noise.",
         "aspects": {"mic": "indoor_only"}, "verified_purchase": True, "created_at": "2026-06-02"},
    ],

    # -------------------------------------------------------------------------
    # 21. Noise ColorFit Pro 5 AMOLED Smartwatch
    # -------------------------------------------------------------------------
    "Noise ColorFit Pro 5 AMOLED Smartwatch": [
        {"author": "Rannvijay Singha", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.95,
         "comment": "1.85-inch AMOLED display with 60Hz refresh rate is silky smooth! 1000 nits peak brightness readable in direct sunlight.",
         "aspects": {"amoled": "vibrant_60hz", "brightness": "1000_nits"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Prince Narula", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Bluetooth calling with TruSync tech connects in seconds. Loud speaker and clear microphone.",
         "aspects": {"bt_calling": "loud_clear", "connectivity": "trusync"}, "verified_purchase": True, "created_at": "2026-07-31"},
        {"author": "Yuvika Chaudhary", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Premium metal finish casing. Jet Black with functional crown dial feels high-end.",
         "aspects": {"crown_dial": "functional", "casing": "metallic_premium"}, "verified_purchase": True, "created_at": "2026-07-25"},
        {"author": "Varun Sood", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.80,
         "comment": "Rapid health tracking: SpO2, continuous heart rate, sleep stages, and stress analysis are accurate.",
         "aspects": {"health_sensors": "reliable", "sleep_tracking": "detailed"}, "verified_purchase": True, "created_at": "2026-07-19"},
        {"author": "Divya Agarwal", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "100+ sports modes with auto workout detection for walking and running.",
         "aspects": {"sports_modes": "comprehensive"}, "verified_purchase": True, "created_at": "2026-07-13"},
        {"author": "Ayush Mehra", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.11,
         "comment": "Battery lasts about 4-5 days with Bluetooth calling active, which is fine but less than advertised 7 days.",
         "aspects": {"battery": "4_to_5_days"}, "verified_purchase": True, "created_at": "2026-07-06"},
        {"author": "Barkha Singh", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.92,
         "comment": "NoiseFit companion app syncs flawlessly with Apple Health and Google Fit. Sleek UI.",
         "aspects": {"app_sync": "smooth", "ui": "clean"}, "verified_purchase": True, "created_at": "2026-06-28"},
        {"author": "Rohan Shah", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.61,
         "comment": "The silicone strap causes mild skin sweating during humid workout sessions. Bought a nylon band.",
         "aspects": {"strap": "sweaty_silicone"}, "verified_purchase": True, "created_at": "2026-06-20"},
        {"author": "Mithila Palkar", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Always-on Display (AOD) has gorgeous analog watch faces. Received compliments.",
         "aspects": {"aod": "stylish_faces"}, "verified_purchase": False, "created_at": "2026-06-12"},
        {"author": "Dhruv Sehgal", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.77,
         "comment": "IP68 water resistant survived swimming pool dips. Terrific smartwatch under ₹3000.",
         "aspects": {"water_resistance": "ip68_swimming"}, "verified_purchase": True, "created_at": "2026-06-04"},
    ],

    # -------------------------------------------------------------------------
    # 22. Fire-Boltt Gladiator Bluetooth Calling Watch
    # -------------------------------------------------------------------------
    "Fire-Boltt Gladiator Bluetooth Calling Watch": [
        {"author": "Gautam Gambhir", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "Massive 1.96-inch HD display! Very easy to read WhatsApp notifications while driving or jogging.",
         "aspects": {"display": "huge_1.96in", "notifications": "easy_read"}, "verified_purchase": True, "created_at": "2026-08-02"},
        {"author": "Harbhajan Singh", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.78,
         "comment": "Looks remarkably like an Apple Watch Ultra. Dark Chrome finish feels solid on wrist.",
         "aspects": {"design": "ultra_inspired", "weight": "substantial"}, "verified_purchase": True, "created_at": "2026-07-28"},
        {"author": "Suresh Raina", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.15,
         "comment": "Calling speaker is loud, but step counter tends to overcount hand gestures as steps by ~10%.",
         "aspects": {"step_counter": "overcounts_gestures", "speaker": "loud"}, "verified_purchase": True, "created_at": "2026-07-22"},
        {"author": "Irfan Pathan", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.82,
         "comment": "123 sports modes and functional rotating crown to scroll menus. Incredible feature set at ₹2199.",
         "aspects": {"features": "loaded", "crown": "scrollable"}, "verified_purchase": True, "created_at": "2026-07-16"},
        {"author": "Yusuf Pathan", "rating": 2.0, "sentiment": "NEGATIVE", "sentiment_score": -0.76,
         "comment": "Companion app DaFit has occasional banner ads. Watch UI feels a bit sluggish compared to Amazfit.",
         "aspects": {"app": "has_ads", "ui_lag": "noticeable"}, "verified_purchase": True, "created_at": "2026-07-09"},
        {"author": "Aakash Chopra", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.72,
         "comment": "Battery lasts 7 days in standby and about 3 full days with heavy Bluetooth calling.",
         "aspects": {"battery": "3_to_7_days"}, "verified_purchase": True, "created_at": "2026-07-02"},
        {"author": "Virender Sehwag", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.81,
         "comment": "Steel Grey strap looks great. Quick magnetic charging works without hassle.",
         "aspects": {"charging": "magnetic", "look": "bold"}, "verified_purchase": False, "created_at": "2026-06-24"},
        {"author": "Ashish Nehra", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.62,
         "comment": "Vibration motor is a bit buzz-like and loud rather than subtle haptic.",
         "aspects": {"vibration": "buzzy"}, "verified_purchase": True, "created_at": "2026-06-16"},
        {"author": "Zaheer Khan", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.75,
         "comment": "Good budget smartwatch for parents or students who want calling on wrist.",
         "aspects": {"value": "budget_friendly"}, "verified_purchase": True, "created_at": "2026-06-08"},
        {"author": "RP Singh", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.06,
         "comment": "Display is TFT, not AMOLED, but bright enough for outdoor usage.",
         "aspects": {"panel": "tft_panel", "outdoor_visibility": "adequate"}, "verified_purchase": True, "created_at": "2026-05-31"},
    ],

    # -------------------------------------------------------------------------
    # 23. Amazfit Bip 5 Ultra Smartwatch
    # -------------------------------------------------------------------------
    "Amazfit Bip 5 Ultra Smartwatch": [
        {"author": "Nitin Gadkari", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.96,
         "comment": "Built-in 4-satellite GPS positioning! Tracks running trails accurately without needing phone. Zepp OS is buttery smooth.",
         "aspects": {"gps": "independent_accurate", "zepp_os": "superb"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Piyush Goyal", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "Sensational 10-day battery life with normal use. BioTracker PPG sensor provides medical-grade heart rate graphs.",
         "aspects": {"battery": "10_days_stellar", "heart_rate": "accurate_biotracker"}, "verified_purchase": True, "created_at": "2026-07-31"},
        {"author": "Anurag Thakur", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "1.91-inch vibrant display with anti-fingerprint coating. Curved glass looks executive.",
         "aspects": {"glass": "curved_anti_smudge", "display": "expansive"}, "verified_purchase": True, "created_at": "2026-07-26"},
        {"author": "Kiren Rijiju", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Amazon Alexa voice assistant built-in. Set timers, check weather, and trigger alarms hands-free.",
         "aspects": {"alexa": "built_in", "voice_commands": "responsive"}, "verified_purchase": True, "created_at": "2026-07-20"},
        {"author": "Jyotiraditya Scindia", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Zepp app ecosystem has mini apps and downloadable calculators, games, and fitness widgets.",
         "aspects": {"mini_apps": "expandable", "ecosystem": "mature"}, "verified_purchase": True, "created_at": "2026-07-14"},
        {"author": "Hardeep Singh Puri", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.80,
         "comment": "Accurate sleep tracking detects REM, light, deep sleep, and brief afternoon power naps.",
         "aspects": {"sleep": "rem_and_nap_tracking"}, "verified_purchase": True, "created_at": "2026-07-08"},
        {"author": "Ashwini Vaishnaw", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.92,
         "comment": "Syncs seamlessly with Strava, Apple Health, and Google Fit. Essential for runners.",
         "aspects": {"strava_sync": "direct_export"}, "verified_purchase": True, "created_at": "2026-07-01"},
        {"author": "Dharmendra Pradhan", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.19,
         "comment": "TFT LCD screen looks clear, though deep blacks are not quite at AMOLED level.",
         "aspects": {"contrast": "lcd_blacks"}, "verified_purchase": False, "created_at": "2026-06-23"},
        {"author": "Mansukh Mandaviya", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.78,
         "comment": "Lightweight curved polycarbonate body. Comfortable to wear 24/7.",
         "aspects": {"ergonomics": "24_7_wearable"}, "verified_purchase": True, "created_at": "2026-06-15"},
        {"author": "G. Kishan Reddy", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.56,
         "comment": "Speaker for Bluetooth calls is adequate in a quiet room, but a bit soft in traffic.",
         "aspects": {"speaker_volume": "soft_outdoors"}, "verified_purchase": True, "created_at": "2026-06-07"},
    ],

    # -------------------------------------------------------------------------
    # 24. Puma Smash v2 Leather Sneakers
    # -------------------------------------------------------------------------
    "Puma Smash v2 Leather Sneakers": [
        {"author": "Shah Rukh Khan", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "Timeless tennis-inspired leather court silhouette. Supple leather upper wipes clean in seconds.",
         "aspects": {"leather": "genuine_supple", "timeless": "court_classic"}, "verified_purchase": True, "created_at": "2026-08-03"},
        {"author": "Gauri Khan", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "White/Navy colorway pairs effortlessly with chinos, selvedge denim, or casual shorts.",
         "aspects": {"versatility": "match_all", "clean_look": "10_10"}, "verified_purchase": True, "created_at": "2026-07-29"},
        {"author": "Aryan Khan", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "SoftFoam+ sockliner makes walking on hard stone pavements surprisingly comfortable.",
         "aspects": {"sockliner": "softfoam", "insole": "cushioned"}, "verified_purchase": True, "created_at": "2026-07-23"},
        {"author": "Suhana Khan", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Durable herringbone patterned rubber outsole provides secure grip on slippery mall floors.",
         "aspects": {"outsole": "herringbone_grip"}, "verified_purchase": True, "created_at": "2026-07-17"},
        {"author": "Juhi Chawla", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Padded collar protects ankle bone from friction. True to size UK 8.",
         "aspects": {"ankle_padding": "plush", "sizing": "spot_on"}, "verified_purchase": True, "created_at": "2026-07-11"},
        {"author": "Karan Johar", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.10,
         "comment": "Leather is slightly stiff on day one. Needs a short 2-day break in period.",
         "aspects": {"break_in": "stiff_first_48h"}, "verified_purchase": True, "created_at": "2026-07-04"},
        {"author": "Farah Khan", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.91,
         "comment": "Great value for genuine leather Puma kicks under ₹2400. Solid stitching.",
         "aspects": {"value": "exceptional_leather"}, "verified_purchase": True, "created_at": "2026-06-26"},
        {"author": "Manish Malhotra", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.76,
         "comment": "Minimalist branding without gaudy logos. Very understated and tasteful.",
         "aspects": {"branding": "subtle_tasteful"}, "verified_purchase": False, "created_at": "2026-06-18"},
        {"author": "Sanjay Kapoor", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.60,
         "comment": "Toe box creases naturally with bending, which is normal for leather but noticeable on white.",
         "aspects": {"creasing": "visible_crease"}, "verified_purchase": True, "created_at": "2026-06-10"},
        {"author": "Maheep Kapoor", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.84,
         "comment": "Very comfortable daily lifestyle sneakers. Excellent quality.",
         "aspects": {"daily_lifestyle": "staple"}, "verified_purchase": True, "created_at": "2026-06-02"},
    ],

    # -------------------------------------------------------------------------
    # 25. Converse Chuck Taylor All Star Street
    # -------------------------------------------------------------------------
    "Converse Chuck Taylor All Star Street": [
        {"author": "Aamir Khan", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.96,
         "comment": "Padded collar and tongue take standard Chucks to another dimension of comfort! Zero heel bite.",
         "aspects": {"street_padding": "game_changer", "heel_comfort": "superior"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Kiran Rao", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Classic diamond tread rubber outsole with authentic Chuck Taylor ankle patch. Heritage streetwear style.",
         "aspects": {"heritage": "iconic_patch", "streetwear": "top_aesthetic"}, "verified_purchase": True, "created_at": "2026-07-30"},
        {"author": "Fatima Sana Shaikh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Canvas upper is thick, durable and stitched with reinforced bar tacks. Heavy duty.",
         "aspects": {"canvas": "heavyweight_durable", "stitching": "reinforced"}, "verified_purchase": True, "created_at": "2026-07-25"},
        {"author": "Sanya Malhotra", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Internal elastic goring band allows easy slip-on wear without untying laces every time.",
         "aspects": {"elastic_tongue": "slip_on_convenience"}, "verified_purchase": True, "created_at": "2026-07-19"},
        {"author": "Zaira Wasim", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.81,
         "comment": "Rubber toe cap protects against scuffs. Optical White accents pop against black canvas.",
         "aspects": {"toe_cap": "protective", "colorway": "classic_contrast"}, "verified_purchase": True, "created_at": "2026-07-13"},
        {"author": "Darsheel Safary", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "SmartSoft foam cushioning insole is much more supportive than classic 1970 flat slabs.",
         "aspects": {"insole": "smartsoft_cushion"}, "verified_purchase": True, "created_at": "2026-07-06"},
        {"author": "Mona Singh", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.18,
         "comment": "Canvas gets slightly wet in heavy rain. Best suited for dry weather and indoor skateparks.",
         "aspects": {"weather": "dry_days_best"}, "verified_purchase": False, "created_at": "2026-06-28"},
        {"author": "Atul Kulkarni", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.92,
         "comment": "True to size UK 9. Outstanding street style kicks that never go out of fashion.",
         "aspects": {"timeless": "forever_fashion"}, "verified_purchase": True, "created_at": "2026-06-20"},
        {"author": "Girish Kulkarni", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.56,
         "comment": "Flat sole has minimal arch support for flat-footed folks running long distances. Casual only.",
         "aspects": {"flat_sole": "low_arch_support"}, "verified_purchase": True, "created_at": "2026-06-12"},
        {"author": "Tanvi Azmi", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Sturdy, comfortable and timeless. Love wearing these with rolled jeans.",
         "aspects": {"outfit_pairing": "perfect"}, "verified_purchase": True, "created_at": "2026-06-04"},
    ],

    # -------------------------------------------------------------------------
    # 26. Adidas Grand Court Baseline Sneakers
    # -------------------------------------------------------------------------
    "Adidas Grand Court Baseline Sneakers": [
        {"author": "Salman Khan", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "70s retro tennis court vibe. Cloudfoam Comfort sockliner provides pillowy underfoot support.",
         "aspects": {"retro_vibe": "70s_court", "sockliner": "cloudfoam_pillow"}, "verified_purchase": True, "created_at": "2026-08-03"},
        {"author": "Katrina Kaif", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "Synthetic leather upper is smooth, durable, and resists rain splatters much better than canvas.",
         "aspects": {"water_resistant": "synthetic_leather", "cleaning": "easy_wipe"}, "verified_purchase": True, "created_at": "2026-07-29"},
        {"author": "Vicky Kaushal", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Three stripes in Cloud White stand out cleanly against Core Black. Premium street look.",
         "aspects": {"stripes": "iconic_three_stripes", "appearance": "sharp"}, "verified_purchase": True, "created_at": "2026-07-23"},
        {"author": "Sunny Kaushal", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Solid cupsole rubber construction delivers long-lasting durability on urban tarmac.",
         "aspects": {"cupsole": "durable_rubber"}, "verified_purchase": True, "created_at": "2026-07-17"},
        {"author": "Sharvari Wagh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.85,
         "comment": "Textile lining keeps foot comfortably cradled without moisture accumulation.",
         "aspects": {"lining": "comfortable"}, "verified_purchase": True, "created_at": "2026-07-10"},
        {"author": "Kabir Khan", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.11,
         "comment": "Weight is slightly noticeable compared to running shoes, but typical for leather court sneakers.",
         "aspects": {"weight": "court_sneaker_average"}, "verified_purchase": True, "created_at": "2026-07-03"},
        {"author": "Mini Mathur", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.91,
         "comment": "Incredible durability! Wore them across 3 airport transits with zero discomfort.",
         "aspects": {"travel": "airport_champion"}, "verified_purchase": True, "created_at": "2026-06-25"},
        {"author": "Ali Abbas Zafar", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.76,
         "comment": "True to size UK 10. Great daily sneakers for work and casual hangouts.",
         "aspects": {"fit": "true_to_size"}, "verified_purchase": False, "created_at": "2026-06-17"},
        {"author": "Arpita Khan", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.58,
         "comment": "Rubber outsole can feel slightly stiff on the first couple of days.",
         "aspects": {"sole_stiffness": "initial_break_in"}, "verified_purchase": True, "created_at": "2026-06-09"},
        {"author": "Aayush Sharma", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "High quality Adidas construction at an affordable ₹2799 price point.",
         "aspects": {"value": "high_rating"}, "verified_purchase": True, "created_at": "2026-06-01"},
    ],

    # -------------------------------------------------------------------------
    # 27. Arctic Fox Slope 30L Tech Backpack
    # -------------------------------------------------------------------------
    "Arctic Fox Slope 30L Tech Backpack": [
        {"author": "Sundar Pichai", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.96,
         "comment": "Exceptional tech backpack! Dedicated padded sleeve protects my 16-inch MacBook Pro securely. External USB charging port is super handy.",
         "aspects": {"laptop_sleeve": "16in_protective", "usb_port": "functional_charging"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Satya Nadella", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.91,
         "comment": "Ergonomic airflow back panel with breathable mesh channels keeps shirts dry during train commutes.",
         "aspects": {"airflow": "back_ventilation", "ergonomics": "anti_sweat"}, "verified_purchase": True, "created_at": "2026-07-31"},
        {"author": "Nandan Nilekani", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Water repellent 400D polyester fabric shrugs off sudden monsoon rain shower. Keeps notebooks dry.",
         "aspects": {"water_repellent": "monsoon_proof", "fabric": "400d_polyester"}, "verified_purchase": True, "created_at": "2026-07-26"},
        {"author": "K. Krithivasan", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.82,
         "comment": "30L volume is spacious enough for tech gadgets, gym shoes, lunch box, and a water bottle.",
         "aspects": {"capacity": "30l_cavernous", "compartments": "well_organized"}, "verified_purchase": True, "created_at": "2026-07-20"},
        {"author": "Salil Parekh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "S-shaped padded shoulder straps distribute heavy load evenly across back without digging in.",
         "aspects": {"straps": "s_curve_padded", "load_distribution": "even"}, "verified_purchase": True, "created_at": "2026-07-14"},
        {"author": "Rishad Premji", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "Smooth SBS dual-direction zippers with rubber pull cords that glide easily.",
         "aspects": {"zippers": "smooth_sbs"}, "verified_purchase": True, "created_at": "2026-07-08"},
        {"author": "C. Vijayakumar", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.12,
         "comment": "Side water bottle pocket is slightly snug for 1-liter thermos flasks. Works fine with 750ml bottles.",
         "aspects": {"bottle_pocket": "snug_for_1l"}, "verified_purchase": True, "created_at": "2026-07-01"},
        {"author": "Thierry Delaporte", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Hidden anti-theft rear zippered pocket is perfect for passport and wallet during flights.",
         "aspects": {"anti_theft": "hidden_pocket"}, "verified_purchase": False, "created_at": "2026-06-23"},
        {"author": "Nitin Rakesh", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.61,
         "comment": "Bag is slightly tall on people under 5'4. Check the dimensions if you have a shorter torso.",
         "aspects": {"height": "tall_profile"}, "verified_purchase": True, "created_at": "2026-06-15"},
        {"author": "Debjani Ghosh", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Charcoal Black looks professional in boardroom meetings and trendy on weekends. Outstanding value at ₹1899.",
         "aspects": {"aesthetic": "tech_corporate", "value": "best_backpack"}, "verified_purchase": True, "created_at": "2026-06-07"},
    ],

    # -------------------------------------------------------------------------
    # 28. Wildcraft Athleisure Gym & Duffle Bag
    # -------------------------------------------------------------------------
    "Wildcraft Athleisure Gym & Duffle Bag": [
        {"author": "Neeraj Ghaywan", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Dedicated ventilated shoe compartment separates dirty gym trainers from clean clothes! Brilliant utility.",
         "aspects": {"shoe_compartment": "ventilated_hygienic", "utility": "thoughtful"}, "verified_purchase": True, "created_at": "2026-08-03"},
        {"author": "Anurag Kashyap", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.89,
         "comment": "Rugged ripstop fabric resists abrasions on locker room floors and airport baggage belts.",
         "aspects": {"durability": "ripstop_tough", "build": "bulletproof"}, "verified_purchase": True, "created_at": "2026-07-30"},
        {"author": "Vikramaditya Motwane", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "35L volume is huge. Easily accommodates gym clothes, protein shaker, lifting belt, and toiletries.",
         "aspects": {"capacity": "35l_spacious", "gym_ready": "complete"}, "verified_purchase": True, "created_at": "2026-07-25"},
        {"author": "Vasan Bala", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.81,
         "comment": "Matte Grey with Volt Lime piping accents looks sporty and high energy.",
         "aspects": {"color": "volt_accent", "sporty": "high"}, "verified_purchase": True, "created_at": "2026-07-19"},
        {"author": "Zoya Akhtar", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "Detachable padded shoulder strap with heavy-duty metal swivel clips that don't twist.",
         "aspects": {"shoulder_strap": "detachable_padded", "hardware": "metal_clips"}, "verified_purchase": True, "created_at": "2026-07-13"},
        {"author": "Reema Kagti", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.78,
         "comment": "Water-resistant PU coating on base protects contents when set down on damp ground.",
         "aspects": {"waterproof_base": "pu_coated"}, "verified_purchase": True, "created_at": "2026-07-06"},
        {"author": "Alankrita Shrivastava", "rating": 3.0, "sentiment": "NEUTRAL", "sentiment_score": 0.08,
         "comment": "Duffle does not have a rigid plastic base board, so it folds softly when partially packed.",
         "aspects": {"base": "soft_folding", "structure": "flexible"}, "verified_purchase": True, "created_at": "2026-06-28"},
        {"author": "Shoojit Sircar", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.92,
         "comment": "Unbelievable price of ₹1499 for Wildcraft durability. Perfect weekender bag.",
         "aspects": {"value": "bargain_flagship", "weekend_trip": "ideal"}, "verified_purchase": True, "created_at": "2026-06-20"},
        {"author": "Gauri Shinde", "rating": 2.5, "sentiment": "NEGATIVE", "sentiment_score": -0.62,
         "comment": "Side mesh pocket is a bit shallow for oversized 1.5L gym water bottles.",
         "aspects": {"mesh_pocket": "shallow"}, "verified_purchase": False, "created_at": "2026-06-12"},
        {"author": "R. Balki", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.76,
         "comment": "Lightweight empty weight and reinforced double-stitched grab handles.",
         "aspects": {"handles": "reinforced", "weight": "light"}, "verified_purchase": True, "created_at": "2026-06-04"},
    ],

    # -------------------------------------------------------------------------
    # 29. Skybags Tech Commuter Laptop Backpack
    # -------------------------------------------------------------------------
    "Skybags Tech Commuter Laptop Backpack": [
        {"author": "Ratan Tata", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.97,
         "comment": "Masterclass in ergonomic engineering. Ultra-padded air-mesh back panel, dedicated quick-access tech organizer, and premium ballistic nylon.",
         "aspects": {"back_panel": "air_mesh_elite", "tech_organizer": "intuitive", "fabric": "ballistic_nylon"}, "verified_purchase": True, "created_at": "2026-08-04"},
        {"author": "Natashaa Stankovic", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.94,
         "comment": "Obsidian Black looks executive in client presentations. Integrated rain cover at bottom pocket saved my laptop during cloudburst.",
         "aspects": {"rain_cover": "built_in_lifesaver", "corporate": "executive_presence"}, "verified_purchase": True, "created_at": "2026-07-31"},
        {"author": "Hardik Pandya", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.90,
         "comment": "Luggage pass-through strap on rear slides over suitcase trolley handle effortlessly. Airport champion.",
         "aspects": {"luggage_strap": "trolley_compatible", "travel": "seamless"}, "verified_purchase": True, "created_at": "2026-07-26"},
        {"author": "Krunal Pandya", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.88,
         "comment": "Fleece-lined sunglasses and tablet pouch prevents screen scratches without needing covers.",
         "aspects": {"fleece_pocket": "anti_scratch"}, "verified_purchase": True, "created_at": "2026-07-20"},
        {"author": "Jasprit Bumrah", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.87,
         "comment": "28L capacity strikes the exact sweet spot between slim commuter silhouette and spacious payload.",
         "aspects": {"capacity": "28l_sweet_spot", "profile": "slim_sleek"}, "verified_purchase": True, "created_at": "2026-07-14"},
        {"author": "Sanjana Ganesan", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.82,
         "comment": "Heavy duty self-repairing YKK zippers that never jam or snag on internal linings.",
         "aspects": {"ykk_zippers": "snag_free"}, "verified_purchase": True, "created_at": "2026-07-08"},
        {"author": "Rohit Sharma", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.95,
         "comment": "Ergonomic sternum chest clip balances heavy MacBook and power brick loads effortlessly.",
         "aspects": {"sternum_strap": "load_reliever"}, "verified_purchase": True, "created_at": "2026-07-02"},
        {"author": "Ritika Sajdeh", "rating": 4.5, "sentiment": "POSITIVE", "sentiment_score": 0.86,
         "comment": "Reinforced wire-cord padded top grab handle makes lifting heavy pack very sturdy.",
         "aspects": {"grab_handle": "wire_reinforced"}, "verified_purchase": True, "created_at": "2026-06-24"},
        {"author": "Shreyas Iyer", "rating": 3.5, "sentiment": "NEUTRAL", "sentiment_score": 0.20,
         "comment": "Premium bag at ₹2299. Shoulder straps take 2-3 days to soften around collarbones.",
         "aspects": {"break_in": "strap_softening"}, "verified_purchase": False, "created_at": "2026-06-16"},
        {"author": "KL Rahul", "rating": 5.0, "sentiment": "POSITIVE", "sentiment_score": 0.93,
         "comment": "Best commuter backpack on the market. Thoughtful cable pass-through channels throughout.",
         "aspects": {"cable_management": "top_grade", "durability": "5_stars"}, "verified_purchase": True, "created_at": "2026-06-08"},
        {"author": "Athiya Shetty", "rating": 4.0, "sentiment": "POSITIVE", "sentiment_score": 0.79,
         "comment": "High quality finish. Holds shape even when completely empty without sagging.",
         "aspects": {"structure": "non_sagging"}, "verified_purchase": True, "created_at": "2026-05-31"},
    ],
}


# =============================================================================
# Amazon-Style AI Review Summaries ("Customers say" & Merits / Demerits)
# Synthesized authentic customer feedback for all Meridian catalog products.
# =============================================================================

PRODUCT_AMAZON_SUMMARIES = {
    "Nike Revolution 6": {
        "customers_say": "Customers find the running shoes great for daily jogging, treadmill sessions, and casual wear, appreciating their lightweight feel, breathable mesh upper, and shock-absorbing foam midsole. The fit receives mixed feedback - while many find them true to size, some customers report that the toe box runs slightly narrow for wider feet. The insole also receives varied comments, with flat-footed runners noting the stock arch padding is rather thin.",
        "merits": [
            "Shock-absorbing foam midsole absorbing impact on road runs",
            "Breathable mesh upper keeps feet well-ventilated and dry",
            "Reliable outsole traction lasting 250+ kilometers",
            "Lightweight construction with stable heel counter"
        ],
        "demerits": [
            "Runs noticeably narrow across the toe box for wide feet",
            "Default insole padding is rather thin for flat feet"
        ],
        "aspect_pills": [
            {"aspect": "Cushioning", "status": "Positive", "pct": 92},
            {"aspect": "Breathability", "status": "Positive", "pct": 88},
            {"aspect": "Fit & Width", "status": "Mixed", "pct": 72},
            {"aspect": "Durability", "status": "Positive", "pct": 85}
        ]
    },

    "Nike Revolution 7": {
        "customers_say": "Customers appreciate the upgraded plush foam cushioning and modern sleek colorways, finding the shoes very supportive for routine road runs. The padded collar and heel lock receive praise for preventing blisters. However, the initial stiffness receives mixed feedback - while the shoes break in nicely after a couple of runs, some note the midfoot fit feels snug upon first wear.",
        "merits": [
            "Plush, upgraded midsole cushioning with softer road landing",
            "Padded collar and secure heel counter preventing blisters",
            "Sleek contemporary aesthetic and durable rubber outsole"
        ],
        "demerits": [
            "Slightly stiff sole out of the box requiring brief break-in",
            "Snug midfoot profile may feel tight for high insteps"
        ],
        "aspect_pills": [
            {"aspect": "Cushioning", "status": "Positive", "pct": 90},
            {"aspect": "Comfort", "status": "Positive", "pct": 88},
            {"aspect": "Flexibility", "status": "Mixed", "pct": 75}
        ]
    },

    "Reebok Floatride": {
        "customers_say": "Customers find the Floatride Energy foam exceptionally springy and responsive, making these shoes a favorite for both treadmill workouts and fast-paced tempo runs. The breathable upper and lightweight chassis are widely praised. Sizing and arch contouring receive mixed feedback - while standard foot shapes find them comfortable, some runners mention that the arch contour is modest and shoelaces can loosen unless double-knotted.",
        "merits": [
            "Springy Floatride Energy foam with high energy return",
            "Lightweight and breathable upper for high-cadence running",
            "Solid value for money in the performance category"
        ],
        "demerits": [
            "Arch support is modest for individuals requiring high contouring",
            "Stock shoelaces can untie easily without a double knot"
        ],
        "aspect_pills": [
            {"aspect": "Energy Return", "status": "Positive", "pct": 94},
            {"aspect": "Weight", "status": "Positive", "pct": 90},
            {"aspect": "Arch Support", "status": "Mixed", "pct": 70}
        ]
    },

    "Adidas Runfalcon 3": {
        "customers_say": "Customers find the shoes very plush and comfortable for casual walking, commuting, and starter 5K runs, appreciating the Cloudfoam cushioning and classic Adidas styling. The weight receives mixed feedback - while sturdy and well-built, some users consider them slightly heavier than minimal road racers. Durability of the rubber outsole is widely appreciated.",
        "merits": [
            "Plush Cloudfoam midsole for all-day walking comfort",
            "Clean classic 3-stripe design suitable for casual wear",
            "Durable rubber outsole with high wear resistance"
        ],
        "demerits": [
            "Slightly heavier in hand compared to ultra-light racers",
            "Breathability is moderate during hot summer midday runs"
        ],
        "aspect_pills": [
            {"aspect": "Walking Comfort", "status": "Positive", "pct": 89},
            {"aspect": "Style", "status": "Positive", "pct": 92},
            {"aspect": "Weight", "status": "Mixed", "pct": 74}
        ]
    },

    "Puma Flyer Runner": {
        "customers_say": "Customers appreciate the SoftFoam+ sockliner that provides step-in ease and cushioning for gym training and short runs. The clean aesthetic and color combinations are popular among buyers. Sizing receives mixed feedback - while lengthwise true to size, several customers note the forefoot feels slightly compact during long-distance runs beyond 8 kilometers.",
        "merits": [
            "SoftFoam+ insole delivers instant step-in cushioning",
            "Versatile styling transitions easily from gym to casual wear",
            "Affordable pricing with solid stitching quality"
        ],
        "demerits": [
            "Forefoot can feel cramped during extended long runs",
            "Outsole grip is best on dry pavement rather than damp trails"
        ],
        "aspect_pills": [
            {"aspect": "Step-in Comfort", "status": "Positive", "pct": 88},
            {"aspect": "Versatility", "status": "Positive", "pct": 85},
            {"aspect": "Long-distance Cushioning", "status": "Mixed", "pct": 72}
        ]
    },

    "ASICS Gel Contend": {
        "customers_say": "Customers praise the rearfoot GEL cushioning technology and AmpliFoam midsole, highlighting superior shock absorption and orthopedic heel support for runners with joint sensitivity. The overall durability and stability receive high marks. The aesthetics receive mixed feedback - while functionally outstanding, some buyers find the design more utilitarian than trendy.",
        "merits": [
            "Rearfoot GEL cushioning absorbs impact and protects knees",
            "Exceptional arch and heel stability for pronation control",
            "High-durability engineered mesh upper and rubber sole"
        ],
        "demerits": [
            "Aesthetic profile is somewhat utilitarian compared to street sneakers",
            "Slightly firm ride before initial 10km break-in period"
        ],
        "aspect_pills": [
            {"aspect": "Shock Absorption", "status": "Positive", "pct": 95},
            {"aspect": "Heel Stability", "status": "Positive", "pct": 92},
            {"aspect": "Aesthetics", "status": "Mixed", "pct": 78}
        ]
    },

    "Reebok Energen Lite": {
        "customers_say": "Customers love the feathery lightweight design and responsive fuel-efficient stride for quick morning 3K to 5K runs. The breathable mesh keeps feet ventilated. Sizing and cushioning receive mixed feedback - while fast and agile, runners seeking maximum plush stack height find the sole relatively low-profile with less squish.",
        "merits": [
            "Ultra-lightweight chassis for agile sprints and warmups",
            "Well-ventilated upper mesh prevents sweat buildup",
            "Great entry price point for budget-conscious runners"
        ],
        "demerits": [
            "Lower stack height with less plush cushioning on hard asphalt",
            "Lacks lateral stability for high-impact cross-training"
        ],
        "aspect_pills": [
            {"aspect": "Weight", "status": "Positive", "pct": 94},
            {"aspect": "Breathability", "status": "Positive", "pct": 90},
            {"aspect": "Plushness", "status": "Mixed", "pct": 68}
        ]
    },

    "Nike Downshifter 12": {
        "customers_say": "Customers appreciate the midfoot fitband system that locks the foot securely, alongside the durable rubber wrap on the outsole. It is widely recommended for students and daily treadmill joggers. The collar padding receives mixed feedback - while snug, some buyers mention that wearing ankle socks is necessary to avoid rubbing during the first few days.",
        "merits": [
            "Midfoot fitband provides supportive lock-in support",
            "Sustainable materials with durable rubber wrap outsole",
            "Clean styling suitable for everyday campus use"
        ],
        "demerits": [
            "Heel collar can cause minor friction without higher socks during break-in",
            "Insole is glued down, making custom insert replacement trickier"
        ],
        "aspect_pills": [
            {"aspect": "Midfoot Support", "status": "Positive", "pct": 90},
            {"aspect": "Durability", "status": "Positive", "pct": 86},
            {"aspect": "Heel Collar", "status": "Mixed", "pct": 73}
        ]
    },

    "Adidas Galaxy 7": {
        "customers_say": "Customers find the Cloudfoam midsole exceptionally soft for long shifts on their feet, casual walks, and light runs. The breathable lining and roomy fit receive positive marks. The flexibility receives mixed feedback - while very cushioned, the shoe has a slightly stiff forefoot flex that favors forward walking over lateral agility.",
        "merits": [
            "Soft Cloudfoam midsole cushions feet during standing shifts",
            "Roomy fit accommodating medium-to-wide foot widths",
            "Attractive color blocking and reflective heel accents"
        ],
        "demerits": [
            "Stiffer forefoot flex than specialized racing flats",
            "Shoe profile feels slightly bulky for fast track sprints"
        ],
        "aspect_pills": [
            {"aspect": "Cushioning", "status": "Positive", "pct": 91},
            {"aspect": "Roominess", "status": "Positive", "pct": 87},
            {"aspect": "Flexibility", "status": "Mixed", "pct": 72}
        ]
    },

    "Puma Softride Enzo": {
        "customers_say": "Customers appreciate the bold slip-on bootie construction and EVA Softride cushioning that delivers great comfort for urban walking and gym workouts. The midfoot TPU cage provides good lateral support. The ease of entry receives mixed feedback - while convenient, some users note the bootie collar can feel tight to pull on with wide feet or high insteps.",
        "merits": [
            "Eye-catching modern streetwear design with prominent Puma branding",
            "Softride EVA foam provides plush all-day underfoot support",
            "TPU cage keeps the midfoot locked during gym training"
        ],
        "demerits": [
            "Bootie collar requires two hands to pull on for wider feet",
            "Not suited for wet grass or muddy trail running"
        ],
        "aspect_pills": [
            {"aspect": "Design & Style", "status": "Positive", "pct": 93},
            {"aspect": "Cushioning", "status": "Positive", "pct": 89},
            {"aspect": "Ease of Entry", "status": "Mixed", "pct": 71}
        ]
    },

    "Skechers Go Run": {
        "customers_say": "Customers rave about the featherlight weight and responsive Ultra GO cushioning, noting that running feels effortless with zero foot fatigue. The Air Cooled Goga Mat insole is widely praised for heat dissipation. Durability of the exposed foam outsole receives mixed feedback - while comfortable, frequent road runners note faster wear on abrasive gravel.",
        "merits": [
            "Ultra GO lightweight cushioning reduces knee strain",
            "Air Cooled Goga Mat insole keeps feet refreshingly cool",
            "Immediate comfort with virtually zero break-in period"
        ],
        "demerits": [
            "Exposed foam pods wear quicker on gravel and sharp asphalt",
            "Upper mesh is thin and may not provide enough warmth in winter"
        ],
        "aspect_pills": [
            {"aspect": "Comfort", "status": "Positive", "pct": 96},
            {"aspect": "Breathability", "status": "Positive", "pct": 92},
            {"aspect": "Sole Durability", "status": "Mixed", "pct": 70}
        ]
    },

    "New Balance Fresh Foam": {
        "customers_say": "Customers love the precision-engineered Fresh Foam midsole, describing the ride as supremely cushioned and luxurious for long-distance 10K road runs. The wide toe box and plush tongue receive outstanding reviews. The price point and weight receive mixed feedback - while top-tier in comfort, it sits at a slightly higher price and has a heavier profile than minimalist racers.",
        "merits": [
            "Engineered Fresh Foam provides cloud-like long-run shock absorption",
            "Generous toe box allows natural toe splay without pinching",
            "High-density Ndurance rubber outsole lasts over 500 kilometers"
        ],
        "demerits": [
            "Slightly higher price point near the budget ceiling",
            "Weight is on the heavier side for competitive sprints"
        ],
        "aspect_pills": [
            {"aspect": "Plush Cushioning", "status": "Positive", "pct": 96},
            {"aspect": "Toe Box Width", "status": "Positive", "pct": 94},
            {"aspect": "Weight", "status": "Mixed", "pct": 76}
        ]
    },

    "Adidas Duramo SL": {
        "customers_say": "Customers find the shoes versatile and supportive for multi-sport gym training, treadmill jogging, and campus walks, praising the Lightmotion midsole and breathable engineered mesh. Sizing receives mixed feedback - while standard sizing fits most, some report the heel lock could be slightly deeper for high-speed sprints.",
        "merits": [
            "Responsive Lightmotion cushioning balances softness with stability",
            "Breathable multi-layer mesh keeps foot odor low",
            "Adiwear outsole delivers dependable traction indoors and outdoors"
        ],
        "demerits": [
            "Heel cup feels somewhat shallow for aggressive sprint starts",
            "Arch contour is neutral and may need an orthotic for high arches"
        ],
        "aspect_pills": [
            {"aspect": "Versatility", "status": "Positive", "pct": 89},
            {"aspect": "Traction", "status": "Positive", "pct": 88},
            {"aspect": "Heel Lock", "status": "Mixed", "pct": 74}
        ]
    },

    "Puma Velocity Nitro": {
        "customers_say": "Customers praise the advanced NITRO foam technology, highlighting an explosive bounce and springy responsiveness that rivals premium race shoes. The Pumagrip rubber outsole is rated as one of the best on wet roads. Sizing receives mixed feedback - while length is accurate, the midfoot is snug and requires careful lace adjustments.",
        "merits": [
            "Nitrogen-infused NITRO foam delivers exceptional rebound and spring",
            "Pumagrip rubber delivers class-leading traction in wet conditions",
            "Reflective details improve visibility during night runs"
        ],
        "demerits": [
            "Snug racing midfoot profile takes time to adjust",
            "Tongue padding is minimal to save weight"
        ],
        "aspect_pills": [
            {"aspect": "Rebound & Bounce", "status": "Positive", "pct": 97},
            {"aspect": "Wet Grip", "status": "Positive", "pct": 98},
            {"aspect": "Fit Profile", "status": "Mixed", "pct": 75}
        ]
    },

    "ASICS Gel Excite": {
        "customers_say": "Customers find the Gel Excite reliable and dependable for entry-to-intermediate runners, praising the rearfoot GEL and AmpliFoam setup for relieving heel impact. The padded ankle collar and soft tongue ensure great daily comfort. Sizing receives mixed feedback - while true to length, runners with wide feet suggest sizing up a half size.",
        "merits": [
            "Rearfoot GEL cushions heel strike on concrete sidewalks",
            "Generously padded ankle collar and plush tongue",
            "Durable construction with solid toe reinforcement"
        ],
        "demerits": [
            "Width runs slightly compact across the ball of the foot",
            "Not designed for fast sub-4 minute kilometer paces"
        ],
        "aspect_pills": [
            {"aspect": "Heel Cushioning", "status": "Positive", "pct": 92},
            {"aspect": "Comfort", "status": "Positive", "pct": 90},
            {"aspect": "Forefoot Width", "status": "Mixed", "pct": 73}
        ]
    },

    "Nike Air Zoom Pegasus 40": {
        "customers_say": "Customers celebrate the Pegasus 40 as a reliable 'workhorse with wings', praising dual Zoom Air units and React foam that provide consistent, energized daily mileage. The durable waffle outsole and redesigned midfoot strap are highlighted. The price point and firmness receive mixed feedback - while exceptionally durable, the ride is firmer than ultra-max plush shoes.",
        "merits": [
            "Dual Zoom Air units deliver snappy, energized toe-offs",
            "React foam midsole maintains consistent cushioning over 600+ km",
            "Redesigned midfoot band prevents lateral foot slippage"
        ],
        "demerits": [
            "Priced at the premium end of the catalog",
            "Ride is on the responsive/firm side rather than plush squishy"
        ],
        "aspect_pills": [
            {"aspect": "Durability", "status": "Positive", "pct": 98},
            {"aspect": "Energy Return", "status": "Positive", "pct": 93},
            {"aspect": "Value", "status": "Mixed", "pct": 78}
        ]
    },

    "Under Armour HOVR Sonic 6": {
        "customers_say": "Customers appreciate the zero-gravity feel of UA HOVR cushioning that absorbs impact and returns energy cleanly during road runs. The engineered spacer mesh upper provides great ventilation and structure. The flexibility receives mixed feedback - while supportive, some find the heel-to-toe transition slightly firm initially.",
        "merits": [
            "UA HOVR foam absorbs shock and preserves leg energy on long runs",
            "Engineered spacer mesh upper is lightweight and structured",
            "External TPU heel counter delivers excellent rearfoot lock"
        ],
        "demerits": [
            "Slightly rigid ride during the first few workout sessions",
            "Outsole rubber adds slight weight to the overall build"
        ],
        "aspect_pills": [
            {"aspect": "Energy Return", "status": "Positive", "pct": 91},
            {"aspect": "Heel Support", "status": "Positive", "pct": 94},
            {"aspect": "Flexibility", "status": "Mixed", "pct": 72}
        ]
    },

    "Sony WH-CH520 Wireless Bluetooth Headphones": {
        "customers_say": "Customers find the headphones fantastic for remote work, college lectures, and travel, praising an incredible 50-hour battery life, lightweight swivel design, and crystal-clear voice microphones. The ear cup design receives mixed feedback - while lightweight, the on-ear cups can cause ear fatigue during continuous listening sessions exceeding 3 hours.",
        "merits": [
            "Massive 50-hour battery life with fast Type-C quick charging",
            "Multi-point Bluetooth connectivity across phone and laptop",
            "Exceptional voice clarity on phone calls and Zoom meetings"
        ],
        "demerits": [
            "On-ear clamping pressure can cause ear discomfort after 3+ hours",
            "Bass profile is balanced rather than rumbling sub-bass"
        ],
        "aspect_pills": [
            {"aspect": "Battery Life", "status": "Positive", "pct": 99},
            {"aspect": "Call Clarity", "status": "Positive", "pct": 92},
            {"aspect": "On-Ear Comfort", "status": "Mixed", "pct": 71}
        ]
    },

    "boAt Airdopes 141 ANC True Wireless": {
        "customers_say": "Customers find the earbuds great value for commute and gym workouts, appreciating the 32dB active noise cancellation, deep punchy bass, and IPX5 sweat resistance. The microphone and touch controls receive mixed feedback - while music playback is fun and bass-heavy, some users report accidental touch triggers and average call quality in noisy outdoor traffic.",
        "merits": [
            "Impressive 32dB active noise cancellation at an affordable price",
            "Deep signature bass tuning popular for workout music",
            "IPX5 sweat and splash resistance for intense cardio"
        ],
        "demerits": [
            "Touch sensors are sensitive and prone to accidental track skips",
            "Microphone picks up ambient background noise in windy streets"
        ],
        "aspect_pills": [
            {"aspect": "ANC Performance", "status": "Positive", "pct": 89},
            {"aspect": "Bass & Audio", "status": "Positive", "pct": 91},
            {"aspect": "Touch Controls", "status": "Mixed", "pct": 69}
        ]
    },

    "JBL Tune 510BT Pure Bass On-Ear": {
        "customers_say": "Customers praise the signature JBL Pure Bass sound that brings hip-hop and electronic music to life with deep punchy lows, alongside a dependable 40-hour battery. The headband padding receives mixed feedback - while foldable and compact, customers with larger head sizes report the headband padding is thin and clamps tightly.",
        "merits": [
            "Signature JBL Pure Bass sound with dynamic 32mm drivers",
            "40 hours of battery life with 5-minute quick charge for 2 hours playback",
            "Hands-free voice assistant integration with Siri and Google"
        ],
        "demerits": [
            "Tight headband clamping force can feel firm on larger heads",
            "Passive isolation is modest compared to active noise cancellation"
        ],
        "aspect_pills": [
            {"aspect": "Bass Response", "status": "Positive", "pct": 95},
            {"aspect": "Battery Life", "status": "Positive", "pct": 94},
            {"aspect": "Clamping Force", "status": "Mixed", "pct": 68}
        ]
    },

    "Noise ColorFit Pro 5 AMOLED Smartwatch": {
        "customers_say": "Customers love the vibrant 1.85-inch AMOLED display with rich colors and crisp outdoor visibility, along with reliable Bluetooth calling and comprehensive 100+ sports tracking modes. The battery life receives mixed feedback - while it lasts up to 5 days normally, keeping Always-On Display (AOD) active drains the battery within 36 hours.",
        "merits": [
            "Stunning high-resolution AMOLED screen with high brightness",
            "Clear Bluetooth calling with built-in microphone and speaker",
            "Sleek metallic finish with comfortable silicone strap"
        ],
        "demerits": [
            "Always-On Display mode reduces battery longevity to 1.5 days",
            "Companion smartphone app requires occasional Bluetooth sync refresh"
        ],
        "aspect_pills": [
            {"aspect": "Display Quality", "status": "Positive", "pct": 97},
            {"aspect": "Bluetooth Calling", "status": "Positive", "pct": 90},
            {"aspect": "AOD Battery", "status": "Mixed", "pct": 70}
        ]
    },

    "Fire-Boltt Gladiator Bluetooth Calling Watch": {
        "customers_say": "Customers appreciate the bold Apple-inspired luxury aesthetics, large 1.96-inch HD display, and seamless Bluetooth calling for quick wrist dials. The heart rate and sleep tracking sensors receive mixed feedback - while steps and time functions work reliably, health sensors show slight variance when compared against medical-grade devices.",
        "merits": [
            "Large 1.96-inch HD screen with smooth crown scrolling",
            "Loud and clear on-wrist calling speaker",
            "Robust metal casing offering a premium flagship watch feel"
        ],
        "demerits": [
            "Fitness and SpO2 sensor accuracy is indicative rather than clinical",
            "Display is TFT LCD rather than deep AMOLED contrast"
        ],
        "aspect_pills": [
            {"aspect": "Appearance & Build", "status": "Positive", "pct": 93},
            {"aspect": "Speaker & Mic", "status": "Positive", "pct": 88},
            {"aspect": "Sensor Accuracy", "status": "Mixed", "pct": 66}
        ]
    },

    "Amazfit Bip 5 Ultra Smartwatch": {
        "customers_say": "Customers praise the ultra-accurate built-in 4-satellite GPS and Zepp OS ecosystem, noting that running routes and heart rate metrics match dedicated sport watches. The 10-day battery life is a standout feature. The display receives mixed feedback - while sharp and responsive, some users wish it featured an AMOLED panel instead of high-res LCD.",
        "merits": [
            "Dedicated multi-satellite GPS tracks runs without needing a phone",
            "Outstanding 10-day battery life under typical daily usage",
            "Comprehensive Zepp OS with downloadable mini apps"
        ],
        "demerits": [
            "Screen is LCD rather than true black AMOLED",
            "Bezel thickness is slightly noticeable around the screen edge"
        ],
        "aspect_pills": [
            {"aspect": "GPS Tracking", "status": "Positive", "pct": 96},
            {"aspect": "Battery Endurance", "status": "Positive", "pct": 98},
            {"aspect": "Screen Contrast", "status": "Mixed", "pct": 74}
        ]
    },

    "Puma Smash v2 Leather Sneakers": {
        "customers_say": "Customers find the shoes clean, stylish, and timeless for casual outings and office Fridays, appreciating the genuine leather upper and SoftFoam+ comfort insert. The break-in period receives mixed feedback - while very durable, the leather is somewhat stiff during the first week before softening comfortably.",
        "merits": [
            "Durable leather upper that wipes clean easily",
            "SoftFoam+ insole absorbs walking impact comfortably",
            "Minimalist tennis silhouette that matches jeans and chinos"
        ],
        "demerits": [
            "Leather upper requires a 3 to 5 day break-in period",
            "Slightly heavy compared to mesh athletic runners"
        ],
        "aspect_pills": [
            {"aspect": "Timeless Style", "status": "Positive", "pct": 94},
            {"aspect": "Leather Durability", "status": "Positive", "pct": 91},
            {"aspect": "Initial Stiffness", "status": "Mixed", "pct": 70}
        ]
    },

    "Converse Chuck Taylor All Star Street": {
        "customers_say": "Customers love the legendary skate silhouette upgraded with padded collar and tongue for enhanced ankle comfort compared to classic thin Chucks. The vulcanized rubber sole provides dependable board grip. Arch support receives mixed feedback - while universally loved for casual wear, flat soles lack high arch support for long walking tours.",
        "merits": [
            "Padded collar and tongue provide far more comfort than classic Chucks",
            "Iconic street style with vulcanized rubber toe cap",
            "Durable canvas and secure lace-up construction"
        ],
        "demerits": [
            "Flat sole provides minimal arch support without custom insoles",
            "Takes slightly longer to dry if caught in heavy monsoon rain"
        ],
        "aspect_pills": [
            {"aspect": "Iconic Aesthetic", "status": "Positive", "pct": 97},
            {"aspect": "Padded Collar", "status": "Positive", "pct": 92},
            {"aspect": "Arch Support", "status": "Mixed", "pct": 65}
        ]
    },

    "Adidas Grand Court Baseline Sneakers": {
        "customers_say": "Customers appreciate the retro 70s tennis court aesthetic and Cloudfoam Comfort sockliner, finding them ideal for everyday college wear and travel. Sizing receives mixed feedback - while length fits as expected, some customers report the toe box feels slightly snug on wider feet during all-day walking.",
        "merits": [
            "Cloudfoam Comfort sockliner delivers pillowy step-in softness",
            "Classic Adidas 3-stripe styling looks great with any casual outfit",
            "Sturdy rubber cupsole provides good traction and stability"
        ],
        "demerits": [
            "Toe box is slightly tapered and may feel snug on broad feet",
            "Synthetic leather requires regular wiping to avoid creasing"
        ],
        "aspect_pills": [
            {"aspect": "Comfort Sockliner", "status": "Positive", "pct": 91},
            {"aspect": "Casual Styling", "status": "Positive", "pct": 95},
            {"aspect": "Toe Room", "status": "Mixed", "pct": 72}
        ]
    },

    "Arctic Fox Slope 30L Tech Backpack": {
        "customers_say": "Customers find the backpack outstanding for university students and tech professionals, praising the padded 15.6-inch laptop sleeve, dedicated USB charging pass-through, and water-repellent fabric. The main zipper receives mixed feedback - while spacious and rugged, some users note the security flap over the zipper can occasionally snag if zipped hastily.",
        "merits": [
            "Padded anti-shock laptop compartment fits up to 15.6-inch devices",
            "Water-repellent fabric and built-in rain cover protect tech gear",
            "Ergonomic breathable back padding distributes heavy book weight"
        ],
        "demerits": [
            "Protective fabric flap can snag on the main zipper if pulled quickly",
            "Side water bottle pocket is snug for wide 1-liter insulated flasks"
        ],
        "aspect_pills": [
            {"aspect": "Laptop Protection", "status": "Positive", "pct": 96},
            {"aspect": "Water Resistance", "status": "Positive", "pct": 93},
            {"aspect": "Zipper Flap", "status": "Mixed", "pct": 74}
        ]
    },

    "Wildcraft Athleisure Gym & Duffle Bag": {
        "customers_say": "Customers love the thoughtful layout featuring a separate ventilated shoe compartment, spacious 35-liter main compartment, and tough ripstop polyester that easily handles gym clothes and weekend getaways. The shoulder strap receives mixed feedback - while the handles are sturdy, customers carrying heavy gym weights wish the shoulder pad had thicker foam.",
        "merits": [
            "Dedicated isolated shoe compartment keeps dirty sneakers away from clothes",
            "Spacious 35-liter storage capacity with internal zippered valuables pocket",
            "Heavy-duty water-resistant ripstop polyester fabric"
        ],
        "demerits": [
            "Detachable shoulder strap padding is relatively thin under heavy loads",
            "Base lacks rubber protective feet for placing on wet locker room floors"
        ],
        "aspect_pills": [
            {"aspect": "Shoe Compartment", "status": "Positive", "pct": 98},
            {"aspect": "Storage Space", "status": "Positive", "pct": 95},
            {"aspect": "Shoulder Padding", "status": "Mixed", "pct": 73}
        ]
    },

    "Skybags Tech Commuter Laptop Backpack": {
        "customers_say": "Customers praise the lightweight multi-compartment organization, stylish geometric accents, and padded shoulder straps for daily office and metro commuting. Fabric thickness receives mixed feedback - while great for light weight and daily transit, some commuters note that the base fabric could be thicker for rough outdoor travel.",
        "merits": [
            "Three spacious zippered compartments with dedicated organizer pockets",
            "Lightweight construction prevents shoulder fatigue during long commutes",
            "Padded air-mesh back panel provides good airflow on warm days"
        ],
        "demerits": [
            "Base fabric is lighter weight and should not be dragged on abrasive concrete",
            "Laptop strap velcro could be slightly longer for thick gaming laptops"
        ],
        "aspect_pills": [
            {"aspect": "Organization Pockets", "status": "Positive", "pct": 94},
            {"aspect": "Comfortable Straps", "status": "Positive", "pct": 91},
            {"aspect": "Base Durability", "status": "Mixed", "pct": 75}
        ]
    }
}


def synthesize_customer_review_analysis(
    product_title: str | None,
    reviews: list[Any] | None,
    attributes: dict | None = None
) -> dict:
    """
    Dynamically compose an Amazon-style 'Customers say' synthesis narrative
    with explicit merits and demerits from arbitrary customer reviews.
    """
    title = product_title or "this product"
    if not reviews:
        return {
            "customers_say": f"Customers find {title} satisfactory for everyday standard use. Verified buyer feedback is currently gathering for this item.",
            "merits": ["Verified merchant catalog quality", "Standard merchant fulfillment warranty"],
            "demerits": ["Limited community review history currently on file"],
            "aspect_pills": [{"aspect": "General Quality", "status": "Neutral", "pct": 75}]
        }

    pos_comments = []
    neg_comments = []
    aspect_counts = {}

    for r in reviews:
        sentiment = (getattr(r, "sentiment", None) or (r.get("sentiment") if isinstance(r, dict) else "POSITIVE")).upper()
        comment = str(getattr(r, "comment", None) or (r.get("comment", "") if isinstance(r, dict) else "")).strip()
        aspects = getattr(r, "aspects", None) or (r.get("aspects") if isinstance(r, dict) else {})
        if isinstance(aspects, dict):
            for k, v in aspects.items():
                label = k.replace("_", " ").title()
                aspect_counts[label] = aspect_counts.get(label, 0) + 1

        if (sentiment == "POSITIVE" or (isinstance(r, dict) and r.get("rating", 4) >= 4.0)) and len(comment) > 15:
            pos_comments.append(comment.split(".")[0].strip())
        elif (sentiment == "NEGATIVE" or (isinstance(r, dict) and r.get("rating", 4) <= 3.0)) and len(comment) > 15:
            neg_comments.append(comment.split(".")[0].strip())

    merits = pos_comments[:3] if pos_comments else ["Reliable daily performance", "Appealing design and good build quality"]
    demerits = neg_comments[:2] if neg_comments else ["Sizing and initial fit may require minor adjustment"]

    lead_aspect = merits[0].lower() if merits else "overall quality"
    second_aspect = merits[1].lower() if len(merits) > 1 else "clean design"
    critique = demerits[0].lower() if demerits else "moderate fit variance"

    narrative = (
        f"Customers find {title} great for daily use, appreciating {lead_aspect} and {second_aspect}. "
        f"Specific aspects receive mixed feedback - while most customers praise its comfort and value, "
        f"some note that {critique}. Overall, customer feedback is largely positive for its intended category."
    )

    aspect_pills = [
        {"aspect": name, "status": "Positive", "pct": 88}
        for name in list(aspect_counts.keys())[:3]
    ] or [{"aspect": "Build & Comfort", "status": "Positive", "pct": 85}]

    return {
        "customers_say": narrative,
        "merits": merits,
        "demerits": demerits,
        "aspect_pills": aspect_pills
    }


def get_amazon_review_analysis(
    product_title: str | None,
    reviews: list[Any] | None = None,
    attributes: dict | None = None
) -> dict:
    """
    Get or synthesize Amazon 'Customers say' review analysis for any product.
    Matches predefined high-fidelity catalog summaries or synthesizes dynamically.
    """
    if product_title and product_title in PRODUCT_AMAZON_SUMMARIES:
        return PRODUCT_AMAZON_SUMMARIES[product_title]

    # Partial match
    if product_title:
        for known_title, summary in PRODUCT_AMAZON_SUMMARIES.items():
            if known_title.lower() in product_title.lower() or product_title.lower() in known_title.lower():
                return summary

    return synthesize_customer_review_analysis(product_title, reviews, attributes)
