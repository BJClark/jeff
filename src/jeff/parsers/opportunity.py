"""Parser for OPPORTUNITIES.md files."""

import re
from dataclasses import dataclass


@dataclass
class Solution:
    """A solution from the opportunity tree."""
    opportunity: str
    title: str
    assumptions: list[str]
    experiment: str


def parse_opportunities(content: str) -> list[Solution]:
    """Extract solutions from an OPPORTUNITIES.md file."""
    solutions = []

    # Find all opportunities
    opp_pattern = r"### Opportunity \d+: ([^\n]+)(.*?)(?=### Opportunity \d+:|## |$)"
    opp_matches = re.findall(opp_pattern, content, re.DOTALL)

    for opp_name, opp_body in opp_matches:
        opp_name = opp_name.strip()

        # Find solutions within this opportunity
        # Pattern: numbered list item with bold title
        sol_pattern = r"\d+\.\s+\*\*\[?([^\]]*?)\]?\*\*(.*?)(?=\d+\.\s+\*\*|\n---|\n###|\Z)"
        sol_matches = re.findall(sol_pattern, opp_body, re.DOTALL)

        for sol_title, sol_body in sol_matches:
            sol_title = sol_title.strip()
            if not sol_title or sol_title.startswith("Solution"):
                continue

            # Extract assumptions
            assumptions = []
            assumption_match = re.search(r"Assumptions?:\s*([^\n]+(?:\n\s+-[^\n]+)*)", sol_body)
            if assumption_match:
                assumption_text = assumption_match.group(1)
                # Could be inline or list
                if "\n" in assumption_text:
                    assumptions = [
                        a.strip().lstrip("-").strip()
                        for a in assumption_text.split("\n")
                        if a.strip().lstrip("-").strip()
                    ]
                else:
                    assumptions = [assumption_text.strip()]

            # Extract experiment
            experiment = ""
            exp_match = re.search(r"Experiment:\s*([^\n]+)", sol_body)
            if exp_match:
                experiment = exp_match.group(1).strip()

            solutions.append(Solution(
                opportunity=opp_name,
                title=sol_title,
                assumptions=assumptions,
                experiment=experiment
            ))

    return solutions
