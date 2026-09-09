import numpy as np
import matplotlib.pyplot as plt

# 1. Define Business Risk Variables (FAIR Model Inputs)
simulations = 10000
attack_probability = 0.15
min_loss = 500000
max_loss = 5000000

# 2. Storage for financial loss results
financial_losses = []

# 3. The Monte Carlo Loop
for _ in range(simulations):
    # Simulate whether an attack occurs
    attack_occurs = np.random.rand() < attack_probability
    
    if attack_occurs:
        # Simulate the financial loss if an attack occurs
        loss = np.random.uniform(min_loss, max_loss)
    else:
        loss = 0  # No loss if no attack occurs
    
    financial_losses.append(loss)

# 4. Terminal Output
average_loss = sum(financial_losses) / simulations
max_simulated_loss = max(financial_losses)
print("\n--- FAIR Cyber Risk Quantification Report ---")
print(f"Total Scenarios Simulated: {simulations:,}")
print(f"Annualized Expected Loss: ${average_loss:,.2f}") 
print(f"Maximum Worst-Case Scenario: ${max_simulated_loss:,.2f}")

# 5. Visualize the Risk 
breach_events = [loss for loss in financial_losses if loss > 0] #removes zero loss events
plt.figure(figsize=(10, 6))
plt.hist(breach_events, bins=50, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Financial Loss in Millions($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Simulated Breach Losses', fontsize=14)
plt.gca().set_xticklabels([f'${int(x/1e6)}M' for x in plt.gca().get_xticks()])
plt.grid(axis='y', alpha=0.75)   
plt.savefig("Risk_Distribution_Chart.png", dpi=300, bbox_inches='tight')
plt.show()

# 6. Create Text File Report
with open("Executive_Report.md", "w") as file:
    file.write("# FAIR Cyber Risk Quantification Report\n")
    file.write(f"- Total Scenarios Simulated: {simulations:,}\n")
    file.write(f"- Annualized Expected Loss: ${average_loss:,.2f}\n")
    file.write(f"- Maximum Worst-Case Scenario: ${max_simulated_loss:,.2f}\n")
    file.write("\n![Risk Curve](Risk_Distribution_Chart.png)")