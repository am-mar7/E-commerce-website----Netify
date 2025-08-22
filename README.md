# 🌐 Netify  

Netify is a modern full-stack web application designed with performance, scalability, and real-world functionality in mind.  
It integrates **payment processing via Stripe**, stores and manages data using a **SQLite database**, and comes with a clean, responsive UI.  

🔗 **Repository:** [github.com/am-mar7/Netify](https://github.com/am-mar7/Netify)  

---

## 🚀 Features
- ⚡ **High performance** backend with clean architecture  
- 💳 **Stripe Payment Gateway** integration for secure transactions  
- 🗄️ **SQLite Database** for persistent and lightweight storage  
- 🎨 Fully **responsive front-end** with modern design principles  
- 🔒 **Authentication & authorization** system for secure user access  
- 🧪 Built-in **testing setup** to ensure reliability  
- 🛠️ Modular & extensible codebase, easy to maintain and scale  

---

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/am-mar7/Netify.git
   cd Netify
   in settings.py put your secret and public key
   you will find them hashd 
   ```

2. **Backend setup**
   ```bash
   cd backend
   pip install -r requirements.txt   # Python dependencies
   python manage.py migrate          # Setup SQLite database
   python manage.py runserver        # Start backend server
   ```

3. **Frontend setup**
   ```bash
   cd frontend
   npm install
   npm start
   ```

4. **Stripe integration**
   - Create a Stripe account and get your API keys  
   - Add them to `.env` inside the `config/` folder:
     ```env
     STRIPE_SECRET_KEY=your_secret_key_here
     STRIPE_PUBLIC_KEY=your_public_key_here
     ```

---

## 📊 Database
- **SQLite** is used for lightweight, serverless storage.  
- Models are defined under `backend/models/`.  
- Database migrations handled via Django ORM.  

---

## 💳 Payment Gateway (Stripe)
- Integrated with **Stripe Checkout** & **PaymentIntents API**.  
- Securely processes payments for orders/services.  
- Full test mode enabled for development.  

---

## 🤝 Contributing
We welcome contributions! Please fork the repo, create a branch, and submit a pull request.  
Check the [issues page](https://github.com/am-mar7/Netify/issues) for pending tasks.  

---

## 📧 Contact
- **Author:** Ammar Alaa Omar  
- **LinkedIn:** [linkedin.com/in/ammar-alaa-am77](https://www.linkedin.com/in/ammar-alaa-am77)  
- **GitHub:** [github.com/am-mar7](https://github.com/am-mar7)  
- **Codeforces:** [codeforces.com/profile/ammaralaa470](https://codeforces.com/profile/ammaralaa470)  
- **Email:** ammaralaa470@gmail.com  

---

⭐ If you like this project, don’t forget to give it a **star** on GitHub!
