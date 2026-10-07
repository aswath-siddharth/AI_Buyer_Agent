from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
    JSON
)
from sqlalchemy.types import TypeDecorator
from sqlalchemy.orm import relationship

try:
    from pgvector.sqlalchemy import Vector
except ImportError:
    Vector = None

from .database import Base


class CompatibleVector(TypeDecorator):
    """
    Cross-dialect vector type:
    - On PostgreSQL: compiles to native pgvector Vector(dim)
    - On SQLite/others: compiles to standard JSON array
    """
    impl = JSON
    cache_ok = True

    def __init__(self, dim=1024, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dim = dim

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql" and Vector is not None:
            return dialect.type_descriptor(Vector(self.dim))
        return dialect.type_descriptor(JSON())

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return value

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        if hasattr(value, "tolist"):
            return value.tolist()
        return value


class Merchant(Base):
    __tablename__ = "merchants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    rating = Column(Float, nullable=False)

    products = relationship(
        "Product",
        back_populates="merchant"
    )


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    merchant_id = Column(
        Integer,
        ForeignKey("merchants.id"),
        nullable=False
    )

    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

    attributes = Column(JSON, nullable=False)

    delivery_eta = Column(String, nullable=False)
    image_url = Column(String, nullable=True)

    # 1024-dimension Amazon Bedrock Titan Text Embeddings vector for pgvector semantic search
    embedding = Column(CompatibleVector(1024), nullable=True)

    merchant = relationship(
        "Merchant",
        back_populates="products"
    )

    reviews = relationship(
        "ProductReview",
        back_populates="product",
        cascade="all, delete-orphan",
        order_by="desc(ProductReview.id)"
    )


class ProductReview(Base):
    __tablename__ = "product_reviews"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
        index=True
    )

    author = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    sentiment = Column(String, nullable=False)  # POSITIVE, NEUTRAL, NEGATIVE
    sentiment_score = Column(Float, nullable=False)  # -1.0 to +1.0
    comment = Column(String, nullable=False)
    aspects = Column(JSON, nullable=True)
    verified_purchase = Column(Boolean, nullable=False, default=True)
    created_at = Column(String, nullable=False)

    product = relationship(
        "Product",
        back_populates="reviews"
    )



class PaymentMandate(Base):
    __tablename__ = "payment_mandates"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float, nullable=False)

    merchant_id = Column(
        Integer,
        ForeignKey("merchants.id"),
        nullable=False
    )

    order_ref = Column(String, nullable=False, unique=True)

    razorpay_order_id = Column(
        String,
        nullable=True,
        unique=True
    )

    expires_at = Column(String, nullable=False)

    single_use = Column(Boolean, nullable=False, default=True)

    used = Column(Boolean, nullable=False, default=False)

    status = Column(
        String,
        nullable=False,
        default="active"
    )


class AuditEvent(Base):
    __tablename__ = "audit_events"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True, nullable=False)
    timestamp = Column(String, nullable=False)
    actor = Column(String, nullable=False)
    action = Column(String, nullable=False)
    status = Column(String, nullable=False, default="INFO")
    mandate_ref = Column(String, nullable=True)
    reasoning = Column(String, nullable=False)
    input_data = Column(JSON, nullable=True)
    output_data = Column(JSON, nullable=True)