import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyCrZn_DbZ6fBew7oSwJUvkjjN1_iXxRWT4",
  authDomain: "miniblog-85dd9.firebaseapp.com",
  projectId: "miniblog-85dd9",
  storageBucket: "miniblog-85dd9.appspot.com",
  messagingSenderId: "929738347454",
  appId: "1:929738347454:web:b0942caddd2bd36f981fef"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

export { db };