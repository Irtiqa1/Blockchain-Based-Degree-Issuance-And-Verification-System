# Blockchain-Based-Degree-Issuance-And-Verification-System
A secure and decentralized platform for issuing, approving, and verifying academic certificates using blockchain technology and Proof of Authority (PoA) consensus. This project ensures tamper-proof records, multi-role authentication, and real-time certificate tracking.
This project is a blockchain-based system designed to streamline the process of issuing, approving, and verifying academic certificates. Traditional methods of certificate management often involve a lot of paperwork, delays, and the risk of fraud or forgery. This system replaces that with a digital, secure, and transparent platform that benefits both students and educational institutions.

At the heart of the system is blockchain technology, which ensures that once a certificate is approved and recorded, it cannot be changed or tampered with. The system uses a Proof of Authority (PoA) consensus model that involves three academic roles: Registrar, Dean, and Controller. Each role is responsible for approving the certificate in sequence. A certificate is only added to the blockchain after it has been verified and approved by all three authorities.

The platform includes a user-friendly login dashboard for students where they can submit certificate requests, view real-time approval status, and download the certificate once it is fully approved. The certificates are generated as downloadable PDF files and include essential information such as the university logo, student details, and a unique certificate hash that proves its authenticity.

This project is developed using Flask for the backend and a combination of HTML, CSS, and JavaScript for the frontend. The system is connected to a PostgreSQL database to manage student data, certificate requests, and approval records. All communication between different roles and nodes happens through secure APIs and local peer-to-peer networking.

The goal of this project is to bring trust, efficiency, and transparency into academic verification processes. It not only improves the experience for students but also helps universities reduce administrative workload and ensure the integrity of their issued degrees.

Whether it is for job applications, higher studies, or public validation, this system provides a modern solution for certificate management and verification in the digital age.
