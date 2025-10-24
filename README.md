
---


# 🏥 Assistant Médical Intelligent

**Description courte :**
Un assistant médical intelligent combinant **Machine Learning (ML)** et **Intelligence Artificielle Générative (LLM + RAG)** pour aider au dépistage précoce des maladies chroniques et soutenir la prise de décision médicale.

---

## 1. Contexte et Problématique

### 1.1 Contexte

Avec l’augmentation des maladies chroniques comme le diabète, les maladies cardiovasculaires et l’hypertension, le suivi médical régulier devient essentiel.
Au Maroc, l’accès aux soins est parfois limité, surtout dans les zones rurales.

**L’IA peut aider :**

* Dépistage précoce des maladies
* Assistance aux médecins dans le diagnostic
* Suivi des patients à distance

### 1.2 Problématique

Comment créer une application capable de :

1. Prédire le risque de maladies chroniques à partir des données des patients.
2. Fournir un **chatbot médical intelligent** utilisant LLM + RAG pour répondre aux questions avec des sources fiables.
3. Faciliter la communication et le suivi entre médecins et patients.

---

## 2. Solution et Objectifs

### 2.1 Solution proposée

Développement d’une **application web complète** comprenant :

* **Module prédictif ML** : pour prédire les risques de maladies (ex : diabète, maladies cardiaques)
* **Chatbot intelligent (LLM + RAG)** : pour répondre aux questions des patients et des médecins
* **Dashboard pour médecins** : pour gérer les patients et consulter leurs résultats

### 2.2 Objectifs

* Fournir aux patients un outil accessible pour **surveiller leur santé**
* Aider les médecins à **prendre des décisions éclairées**
* Garantir la **confidentialité et la sécurité** des données médicales

---

## 3. Description Fonctionnelle

### 3.1 Fonctionnalités principales

1. **Inscription et authentification** pour patients et médecins
2. **Saisie et gestion des données médicales**
3. **Prédiction des risques** via le module ML
4. **Chatbot médical intelligent** avec LLM + RAG
5. **Dashboard pour médecins** : visualisation, suivi, alertes

### 3.2 Cas d’utilisation

* **Patient :**

  1. Créer un compte
  2. Saisir ses données médicales
  3. Consulter ses prédictions
  4. Poser des questions au chatbot

* **Médecin :**

  1. Se connecter au dashboard
  2. Gérer les patients et leurs données
  3. Visualiser les risques prédits
  4. Interagir avec le chatbot en mode expert

---

## 4. Technologies utilisées

| Partie          | Technologie            |
| --------------- | ---------------------- |
| Backend         | FastAPI (Python)       |
| Frontend        | React + TailwindCSS    |
| Base de données | PostgreSQL             |
| IA/ML           | Scikit-learn, PyTorch  |
| LLM/RAG         | HuggingFace, LangChain |
| Vector DB       | FAISS ou Pinecone      |
| Infrastructure  | Docker, GitHub, MLflow |

---

## 5. Architecture du système

### 5.1 Schéma global

```text
Frontend (React)
        ↓
   Backend (FastAPI)
        ↓
   ML / LLM services
        ↓
Base de données (PostgreSQL + FAISS)
```

### 5.2 Déroulement du traitement

1. Le **patient saisit ses données médicales** sur l’interface.
2. Les **données sont envoyées au backend** FastAPI.
3. Le **module ML** prédit le risque de maladie.
4. Le **LLM + RAG** fournit une explication médicale claire et détaillée.
5. Les **résultats sont affichés au patient** et **sauvegardés pour le médecin** sur son dashboard.

---

## 6. Fonctionnement 

1. **Inscription / Connexion**

   * Patient ou médecin crée son compte avec email et mot de passe
   * Connexion sécurisée via JWT

2. **Saisie des données**

   * Patient remplit un formulaire avec âge, poids, habitudes, antécédents médicaux, etc.

3. **Prédiction du risque**

   * Le backend traite les données
   * Le modèle ML retourne un **score de risque** (ex : faible, moyen, élevé)

4. **Chatbot médical**

   * Patient ou médecin peut poser une question
   * Le LLM utilise RAG pour fournir une **réponse basée sur des sources fiables**

5. **Dashboard médecin**

   * Visualisation de tous les patients
   * Alertes si un risque est élevé
   * Accès aux historiques et explications

---

## 7. Installation et Lancement

### 7.1 Prérequis

* Python 3.x
* Node.js + npm/yarn (pour React)
* Docker & Docker Compose
* PostgreSQL

### 7.2 Lancer l’application localement

1. **Cloner le projet :**

```bash
git clone https://github.com/IKRAM1919/assistant-medical-intelligent.git
cd assistant-medical-intelligent
```

2. **Backend :**

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

3. **Frontend :**

```bash
cd frontend
npm install
npm start
```

4. **Docker  :**

```bash
docker-compose up --build
```

5. **Accéder :**

* Frontend : `http://localhost:3000`
* API Swagger : `http://localhost:8000/docs`

---

## 8. Sécurité et confidentialité

* **Mot de passe hashé** avec bcrypt
* **Authentification JWT** pour sécuriser les endpoints
* **Données médicales anonymisées** et sauvegardées en toute sécurité
* Respect de **RGPD et AI Act**

---

## 9. Objectifs pédagogiques

* Comprendre le fonctionnement d’un **système IA complet** (ML + LLM)
* Développer une **API sécurisée avec FastAPI**
* Créer un **dashboard interactif** pour visualiser les résultats
* Apprendre à **containeriser et déployer** une application avec Docker

---

## 10. Conclusion

Ce projet combine **IA traditionnelle et IA générative** pour créer un **assistant médical intelligent**.

**Avantages :**

* Réduction de la charge des médecins
* Amélioration du suivi patient
* Accès facilité à des informations médicales fiables

---

## 📂 Structure du projet

```
assistant-medical-intelligent/
├─ backend/
│  ├─ app/
│  │  ├─ main.py          # FastAPI
│  │  ├─ model.py         # ML model + prédiction
│  │  ├─ llm_chat.py      # Chatbot LLM + RAG
│  │  ├─ schemas.py       # Pydantic models
│  │  └─ database.py      # Connexion PostgreSQL 
│  └─ requirements.txt
├─ frontend/
│  ├─ public/
│  ├─ src/
│  │  ├─ App.js
│  │  ├─ components/
│  │  │  ├─ Dashboard.js
│  │  │  ├─ PatientForm.js
│  │  │  └─ Chatbot.js
│  │  └─ services/
│  │      └─ api.js       # appel API backend
│  └─ package.json
├─ models/
│  ├─ best_medical_diagnosis_model.pkl
│  └─ label_encoder.pkl
└─ data/                  # CSV ou documents médicaux

```

---





