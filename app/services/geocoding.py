"""Geocoding helpers for vendor onboarding workflow."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def geocoding_step_0(records: list[dict], limit: int = 185) -> list[dict]:
    """Apply geocoding rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("geocoding step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def geocoding_step_1(records: list[dict], limit: int = 413) -> list[dict]:
    """Apply geocoding rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("geocoding step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def geocoding_step_2(records: list[dict], limit: int = 179) -> list[dict]:
    """Apply geocoding rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("geocoding step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def geocoding_step_3(records: list[dict], limit: int = 213) -> list[dict]:
    """Apply geocoding rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("geocoding step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def geocoding_step_4(records: list[dict], limit: int = 85) -> list[dict]:
    """Apply geocoding rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("geocoding step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def geocoding_step_5(records: list[dict], limit: int = 61) -> list[dict]:
    """Apply geocoding rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("geocoding step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def geocoding_step_6(records: list[dict], limit: int = 336) -> list[dict]:
    """Apply geocoding rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("geocoding step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def geocoding_step_7(records: list[dict], limit: int = 115) -> list[dict]:
    """Apply geocoding rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("geocoding step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def geocoding_step_8(records: list[dict], limit: int = 59) -> list[dict]:
    """Apply geocoding rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("geocoding step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
