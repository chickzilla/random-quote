<template>
  <div class="auth-container">
    <div class="form-box">
      <h2>Login</h2>

      <input v-model="email" type="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />

      <button :disabled="!isValid" @click="signUp">Sign In</button>

      <p class="switch-text">
        Don't have any account?
        <router-link to="/auth/signUp" class="sign-Up">Sign Up</router-link>
      </p>

      <p v-if="error" class="error">{{ error }}</p>
      <p v-if="success" class="success">{{ success }}</p>
    </div>
  </div>
</template>

<script setup>
import { login, register } from '@/services/authService'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const error = ref('')
const success = ref('')
const router = useRouter()

const isValid = computed(() => {
  return email.value && password.value
})

const signUp = async () => {
  if (!isValid.value) {
    error.value = 'Please fill all fields correctly.'
    return
  }

  error.value = ''
  try {
      await login(email.value, password.value)
      success.value = 'Logged in successfully!'
      setTimeout(() => {
        router.push('/')
      }, 1500)
    } catch (e) {
      console.error(e)
      error.value = e
    }
}
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f2f5f9;
}

.form-box {
  background-color: white;
  padding: 40px;
  border-radius: 10px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 24px;
  color: #f3b98f;
  font-weight: bold;
}

input {
  display: block;
  width: 100%;
  padding: 12px;
  margin-bottom: 16px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 6px;
  outline: none;
}

button {
  width: 100%;
  background-color: #f3b98f;
  border: none;
  padding: 12px;
  font-weight: bold;
  color: white;
  font-size: 16px;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover:enabled {
  background-color: #f0a76a;
}

button:disabled {
  background-color: #ddd;
  cursor: not-allowed;
}

.switch-text {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: darkblue;

}

.switch-text a {
  color: darkblue;
  font-weight: 500;
  text-decoration: none;
}

.switch-text a:hover {
  text-decoration: underline;
}

.error {
  color: red;
  text-align: center;
  margin-top: 10px;
}

.success {
  color: green;
  text-align: center;
  margin-top: 10px;
}
</style>
