# Chapter 1 — The Machine Learning Landscape

This chapter introduces the **foundations of Machine Learning**, focusing on *what machine learning is*, *why it is useful*, *how ML systems are categorized*, and *what can go wrong in practice*.  
The goal is to build a **mental map** of the field before diving into implementation.

---

## 1. What Is Machine Learning?
Machine Learning is the field of study that enables computers to **learn from data** and **improve their performance on a task through experience**, without being explicitly programmed.

A system learns from:
- **Experience (data)**
- **Task**
- **Performance measure**

---

## 2. Why Use Machine Learning?
Machine learning is especially useful when:
- Explicit rules are **too complex or unknown**
- Systems must **adapt to changing data**
- Large volumes of data contain **hidden patterns**
- Automation and scalability are required

Typical applications include spam filtering, recommendation systems, anomaly detection, and natural language processing.

---

## 3. Types of Machine Learning Systems

### By supervision
- **Supervised learning**
- **Unsupervised learning**
- **Semi-supervised learning**
- **Self-supervised learning**
- **Reinforcement learning**

### By learning style
- **Batch learning**
- **Online learning**

### By generalization strategy
- **Instance-based learning**
- **Model-based learning**

---

## 4. Supervised Learning
Supervised learning uses **labeled training data**.

Common tasks:
- **Regression** -> predict continuous values
- **Classification** -> predict discrete labels

---

## 5. Unsupervised Learning
Unsupervised learning works with **unlabeled data**.

Common tasks:
- **Clustering**
- **Dimensionality reduction**
- **Anomaly detection**
- **Association rule learning**

---

## 6. Semi-Supervised & Self-Supervised Learning
- **Semi-supervised learning** uses a small labeled dataset combined with a large unlabeled dataset.
- **Self-supervised learning** automatically generates labels from the data itself and is widely used in modern deep learning.

---

## 7. Reinforcement Learning
An **agent** interacts with an **environment**, taking actions and receiving rewards or penalties.  
The goal is to learn a **policy** that maximizes cumulative reward.

Common in robotics, games, and control systems.

---

## 8. Batch vs Online Learning
- **Batch learning**: trained once on a fixed dataset
- **Online learning**: learns incrementally as new data arrives

Online learning is suitable for large datasets and evolving environments but requires careful monitoring.

---

## 9. Instance-Based vs Model-Based Learning
- **Instance-based learning**: compares new data to stored examples using similarity measures
- **Model-based learning**: learns a model by optimizing parameters and uses it to make predictions

---

## 10. Typical Machine Learning Workflow
1. Define the problem
2. Collect and explore data
3. Prepare the data
4. Select a model
5. Train the model
6. Tune hyperparameters
7. Evaluate on test data
8. Deploy and monitor

---

## 11. Main Challenges in Machine Learning
- Insufficient training data
- Non-representative or biased data
- Poor-quality data (noise, missing values)
- Irrelevant features
- Overfitting and underfitting
- Data leakage
- Data mismatch between training and real-world data

---

## 12. Training, Validation, and Test Sets
- **Training set**: used to learn model parameters
- **Validation set**: used to tune hyperparameters and select models
- **Test set**: used only for final evaluation

A **train-dev set** may be used when training and test data come from different distributions to diagnose data mismatch.

---

## 13. Key Takeaways
- Machine learning is about **generalization**, not memorization
- Data quality and representativeness are often more important than model choice
- Proper evaluation requires strict separation of datasets
- Most ML failures come from **data and evaluation mistakes**, not algorithms

---

## Status
Chapter 1 completed  
 Exercises reviewed and corrected  
📘 Ready to move on to **Chapter 2: End-to-End Machine Learning Project**