<template>
  <div
    class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-blue-100 to-white"
  >
    <h1 class="text-4xl font-bold mb-10 text-blue-700">羽球開團吧！</h1>
    <div class="flex gap-6">
      <router-link to="/create">
        <button
          class="px-8 py-3 bg-blue-500 text-white rounded-lg shadow hover:bg-blue-600 transition"
        >
          建立房間
        </button>
      </router-link>
      <router-link to="/join">
        <button
          class="px-8 py-3 bg-green-500 text-white rounded-lg shadow hover:bg-green-600 transition"
        >
          加入房間
        </button>
      </router-link>
    </div>
  </div>
</template>
