// products.js
import axios from 'axios';

export const products = {
  namespaced: true,
  state: () => ({
    products: [],
    categories: []
  }),
  mutations: {
    SET_PRODUCTS(state, products) {
      state.products = products;
    },
    SET_CATEGORIES(state, categories) {
      state.categories = categories;
    }
  },
  actions: {
    fetchProducts({ commit }) {
      axios.get('/products')
        .then(response => {
          commit('SET_PRODUCTS', response.data);
        })
        .catch(error => {
          console.error('Error fetching products:', error);
        });
    },
    fetchCategories({ commit }) {
      axios.get('/categories')
        .then(response => {
          commit('SET_CATEGORIES', response.data);
        })
        .catch(error => {
          console.error('Error fetching categories:', error);
        });
    }
  }
};
