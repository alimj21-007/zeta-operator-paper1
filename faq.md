# Frequently Asked Questions (FAQ)

This document answers common questions about the **Zeta Operator Project**.

---

## ⚙️ Configuration & Parameters

**Q: How do I change the parameter `s` or grid size?**  
A: Open `config.json` in the project root and edit the values for `s` and `grid_size`. Then re-run `main.py`.

**Q: Can I increase the number of eigenpairs computed?**  
A: Yes. In `config.json`, adjust the `num_eigs` parameter to the desired number.

**Q: How do I change the domain of computation?**  
A: Modify the `domain` field in `config.json`. For example:  
```json
"domain": [0.0, 1.0]

]

📊 Outputs & Interpretation

Q: Where are the outputs saved?A: All CSV and PNG files are saved in the project root (or code/ if run from there). A summary of all outputs is listed in summary_table.csv.

Q: What does convergence_plot.png show?A: It visualizes the convergence of trace and Hilbert–Schmidt norm as grid size increases.

Q: What is inside summary_table.csv?A: It lists all generated outputs with their filename, type, and description.

Q: What is the purpose of log.txt?A: It records every action performed by the pipeline, ensuring reproducibility.

🔧 Customization

Q: Can I add my own kernel?A: Yes. Define a new function in kernels.py and update config.json to use it.

Q: Can I change the visualization style of plots?A: Yes. Modify plots.py to adjust colormaps, labels, or figure size.

🐞 Troubleshooting

Q: I get a ModuleNotFoundError. What should I do?A: Make sure you installed dependencies with:

pip install -r requirements.txt

Q: My plots look empty or incorrect.A: Check that your grid size is large enough and parameters in config.json are valid.

Q: The program runs slowly. How can I speed it up?A: Reduce grid_size or num_eigs in config.json. For large experiments, consider running on a machine with more memory/CPU.

📌 Notes

Always check log.txt for details of what happened during execution.

For reproducibility, avoid editing code directly—use config.json whenever possible.
