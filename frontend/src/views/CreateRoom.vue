<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-white">
    <h2 class="text-2xl font-bold mb-6 text-blue-800">建立房間</h2>
    <form
      class="w-full max-w-xs bg-blue-50 p-6 rounded shadow flex flex-col gap-4"
      @submit.prevent="onSubmit"
      aria-label="建立房間表單"
    >
      <div>
        <label for="owner" class="block mb-1 font-medium text-gray-800"
          >開團者名稱</label
        >
        <input
          id="owner"
          v-model="form.owner"
          class="input"
          required
          placeholder="請輸入你的名字"
          autocomplete="username"
        />
      </div>
      <div>
        <label for="court_count" class="block mb-1 font-medium text-gray-800"
          >場地數量</label
        >
        <input
          id="court_count"
          v-model.number="form.court_count"
          type="number"
          min="1"
          class="input"
          required
        />
      </div>
      <div>
        <label
          for="players_per_court"
          class="block mb-1 font-medium text-gray-800"
          >每場人數</label
        >
        <input
          id="players_per_court"
          v-model.number="form.players_per_court"
          type="number"
          min="2"
          class="input"
          required
        />
      </div>
      <div>
        <label for="password" class="block mb-1 font-medium text-gray-800"
          >房間密碼</label
        >
        <input
          id="password"
          v-model="form.password"
          type="password"
          class="input"
          required
          placeholder="請設定密碼"
          autocomplete="new-password"
        />
      </div>
      <button
        type="submit"
        class="w-full py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2"
        aria-label="建立房間"
      >
        建立
      </button>
      <div v-if="error" class="text-red-600 text-sm mt-2" role="alert">
        {{ error }}
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();
const form = ref({
  owner: "",
  court_count: 1,
  players_per_court: 4,
  password: "",
});
const error = ref("");

async function onSubmit() {
  error.value = "";
  try {
    const res = await axios.post(
      "http://localhost:8000/create_room",
      form.value
    );
    router.push({ name: "Room", params: { roomId: res.data.room_id } });
  } catch (e) {
    error.value = e.response?.data?.detail || e.message || "建立房間失敗";
  }
}
</script>

<style scoped>
.input {
  width: 100%;
  padding: 0.5rem 0.75rem;
  border: 1px solid #cbd5e1;
  border-radius: 0.375rem;
  outline: none;
  font-size: 1rem;
  background: #fff;
  color: #1e293b;
}
.input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 2px #60a5fa33;
}
</style>
