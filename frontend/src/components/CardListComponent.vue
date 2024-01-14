<!-- CardListComponent.vue -->
<template>
  <div>
    <div v-for="card in cards" :key="card.id">{{ card.code }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cards: []
    };
  },
  created() {
    this.fetchCards();
  },
  methods: {
    async fetchCards() {
      const response = await axios.get('http://localhost:8000/cards');
      this.cards = response.data;
    }
  }
};
</script>
