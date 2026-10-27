from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
CASE = ROOT / "references" / "synthetic-case.md"


class PackageTests(unittest.TestCase):
    def test_skill_contract_and_references(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: multi-channel-persona-research\n"))
        self.assertIn("\ndescription: ", text.split("---", 2)[1])
        for heading in (
            "Implementation Basis and Dependencies",
            "Inputs",
            "Outputs",
            "Workflow",
            "Stop Conditions",
        ):
            self.assertIn("## " + heading, text)
        refs = re.findall(r"\]\((references/[^)]+)\)", text)
        self.assertEqual(
            set(refs),
            {"references/collection-playbook.md", "references/synthetic-case.md"},
        )
        for ref in refs:
            self.assertTrue((ROOT / ref).is_file(), ref)

    def test_synthetic_case_is_internally_consistent(self):
        text = CASE.read_text(encoding="utf-8")
        defined = set(re.findall(r"^\| (SIM-\d{2}) \|", text, re.MULTILINE))
        cited = set(re.findall(r"SIM-\d{2}", text))
        self.assertEqual(defined, {f"SIM-{i:02d}" for i in range(1, 7)})
        self.assertEqual(cited, defined)
        for phrase in ("完全虚构", "没有真实流量", "随机分配", "护栏指标"):
            self.assertIn(phrase, text)

    def test_public_package_has_no_source_identifiers(self):
        docs = [ROOT / "SKILL.md", CASE, ROOT / "references" / "collection-playbook.md", ROOT / "README.md", ROOT / "README.en.md"]
        body = "\n".join(path.read_text(encoding="utf-8") for path in docs)
        for forbidden in ("Jeep", "Bronco", "F-150", "Joytutus", "TRAILFORM", "facebook-ai", "A1306", "benliu2021"):
            self.assertNotIn(forbidden, body)
        self.assertNotRegex(body, r"[A-Za-z]:[/\\]Users[/\\]")
        self.assertNotRegex(body, r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")


if __name__ == "__main__":
    unittest.main()
