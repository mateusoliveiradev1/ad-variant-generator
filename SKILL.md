---
name: Ad Creative Variant Generator — Persona-Mapped Copy Validation Engine
description: "Analyze, Orchestrate, and Validate operations to: Synthesizes 3 structured ad copy variants (Fear, Gain, Logic hooks) mapped to a specific buyer persona, then deterministically validates every character against platform limits (Meta, LinkedIn, X) using Python before outputting a ready-to-upload Variant Matrix. ROI: eliminates manual character counting and ensures zero platform-rejected copy submissions."
---

# 🎯 Goal
Deterministically execute operations for Ad Creative Variant Generator — Persona-Mapped Copy Validation Engine, ensuring auditable and precise outcomes without hallucination.

# 🧠 Decision Tree & Chain-of-Thought
1. **Analyze:** Parse the user's request, examine existing artifacts in the workspace, and identify the exact constraints and goals before taking action.
2. **Execute:** Run explicit scripts inside the `scripts/` directory to perform heavy lifting, API calls, or data transformations natively.
3. **Verify:** Rigorously test the outputs against the initial constraints. If errors occur, self-correct using progressive iterations.

# 💾 Artifact Persistence (Dual-Write Pattern)
* **Phase 1 (Draft):** Todos os rascunhos, análises e iterações DEVEM ser feitos na pasta `brain/` e apresentados ao usuário.
* **Phase 2 (Permanent):** APENAS após a aprovação do usuário ("Looks good"), copie o artefato final para `project/docs/` e atualize o `ARTIFACT_REGISTRY.md`.

# 🤝 Team Collaboration & Delegation
* **Related Skills:** [Cross-functional AI Agents, Specialized Data Pipelines]
* **When to Delegate:** Se a tarefa sair do escopo desta skill, PARE e recomende o uso de outra skill do catálogo.

# 🚫 Constraints
* NUNCA passe de 500 linhas neste arquivo. Lógicas complexas devem ser delegadas para a pasta `scripts/`.
* NÃO alucine dados. Use saídas determinísticas.
