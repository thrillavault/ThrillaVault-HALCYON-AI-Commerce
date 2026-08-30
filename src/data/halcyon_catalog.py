# SPDX-License-Identifier: Apache-2.0
"""HALCYON NFT catalog for ThrillaVault AI recommendations."""

from .product_catalog import ProductData


HALCYON_PRODUCTS: list[ProductData] = [
    {
        "id": "halcyon_core_emerald",
        "sku": "HLC-CE-001",
        "name": "HALCYON Core Emerald",
        "price_cents": 0,
        "stock_count": 700,
        "min_margin": 0.0,
        "image_url": "/halcyon/core-emerald.jpeg",
        "category": "digital-collectibles",
        "subcategory": "automotive-nft",
        "description": (
            "The foundation tier of the HALCYON collection. Core Emerald "
            "features the signature ThrillaVault emerald visual identity and "
            "provides an accessible entry into the HALCYON collector ecosystem."
        ),
        "attributes": [
            "core-tier",
            "emerald",
            "digital-collectible",
            "automotive-art",
            "accessible",
            "supply-700",
            "price-tbd",
        ],
        "lifecycle": "prelaunch",
        "demand_velocity": "unknown",
    },
    {
        "id": "halcyon_obsidian",
        "sku": "HLC-OB-001",
        "name": "HALCYON Obsidian",
        "price_cents": 0,
        "stock_count": 200,
        "min_margin": 0.0,
        "image_url": "/halcyon/obsidian.jpeg",
        "category": "digital-collectibles",
        "subcategory": "automotive-nft",
        "description": (
            "A limited HALCYON edition built around a darker black and emerald "
            "visual treatment for collectors seeking greater scarcity and a "
            "more exclusive ThrillaVault presentation."
        ),
        "attributes": [
            "limited-tier",
            "obsidian",
            "black",
            "emerald",
            "scarce",
            "supply-200",
            "price-tbd",
        ],
        "lifecycle": "prelaunch",
        "demand_velocity": "unknown",
    },
    {
        "id": "halcyon_sovereign_gold",
        "sku": "HLC-SG-001",
        "name": "HALCYON Sovereign Gold",
        "price_cents": 0,
        "stock_count": 75,
        "min_margin": 0.0,
        "image_url": "/halcyon/sovereign-gold.jpeg",
        "category": "digital-collectibles",
        "subcategory": "automotive-nft",
        "description": (
            "A rare gold-accented HALCYON edition for collectors prioritizing "
            "luxury presentation, reduced supply, and elevated status within "
            "the ThrillaVault collector ecosystem."
        ),
        "attributes": [
            "rare-tier",
            "sovereign",
            "gold",
            "luxury",
            "collector-status",
            "supply-75",
            "price-tbd",
        ],
        "lifecycle": "prelaunch",
        "demand_velocity": "unknown",
    },
    {
        "id": "halcyon_animated_xr",
        "sku": "HLC-AX-001",
        "name": "HALCYON Animated XR",
        "price_cents": 0,
        "stock_count": 20,
        "min_margin": 0.0,
        "image_url": "/halcyon/animated-xr.jpeg",
        "category": "digital-collectibles",
        "subcategory": "animated-automotive-nft",
        "description": (
            "An ultra-limited animated HALCYON edition showcasing XR-inspired "
            "motion, VisionStack visual cues, and futuristic vehicle artwork "
            "for collectors seeking dynamic digital media."
        ),
        "attributes": [
            "ultra-rare-tier",
            "animated",
            "xr",
            "visionstack",
            "dynamic-media",
            "supply-20",
            "price-tbd",
        ],
        "lifecycle": "prelaunch",
        "demand_velocity": "unknown",
    },
    {
        "id": "halcyon_founder_one_of_one",
        "sku": "HLC-F1-001",
        "name": "HALCYON Founder 1/1",
        "price_cents": 0,
        "stock_count": 5,
        "min_margin": 0.0,
        "image_url": "/halcyon/founder-one-of-one.jpeg",
        "category": "digital-collectibles",
        "subcategory": "founder-automotive-nft",
        "description": (
            "One of five individually distinguished Founder artworks at the "
            "highest HALCYON rarity level, intended for top-tier collectors "
            "seeking maximum scarcity and archival significance."
        ),
        "attributes": [
            "founder-tier",
            "one-of-one-artwork",
            "maximum-scarcity",
            "archival",
            "exclusive",
            "five-unique-tokens",
            "price-tbd",
        ],
        "lifecycle": "prelaunch",
        "demand_velocity": "unknown",
    },
]