export const cart = {
  namespaced: true,
  state: () => ({
    items: [],
    isCartDropdownVisible: false
  }),
  getters: {
    totalItems: (state) => state.items.reduce((total, item) => total + item.quantity, 0),
    isDropdownVisible: state => state.isCartDropdownVisible,
  },
  mutations: {
    SET_CART_ITEMS(state, items) {
      state.items = items;
    },
    // 当添加或移除商品时，确保调用 saveCart
    ADD_TO_CART(state, product) {
    const existingProduct = state.items.find(item => item.id === product.id);
    if (existingProduct) {
      existingProduct.quantity++;
    } else {
      state.items.push({ ...product, quantity: 1 });
    }
    },
    REMOVE_FROM_CART(state, productId) {
      state.items = state.items.filter((item) => item.id !== productId);
      this.dispatch('cart/saveCart');
    },
    TOGGLE_CART_DROPDOWN(state) {
      state.isCartDropdownVisible = !state.isCartDropdownVisible;
    },
  },
  actions: {
    loadCart({ commit }) {
      const cart = localStorage.getItem('cart');
      if (cart) {
        commit('SET_CART_ITEMS', JSON.parse(cart));
      }
    },
    saveCart({ state }) {
      localStorage.setItem('cart', JSON.stringify(state.items));
    },
    addToCart({ commit, dispatch }, product) {
    commit('ADD_TO_CART', product);
    dispatch('saveCart');
  },
    removeFromCart({ commit }, productId) {
      commit('REMOVE_FROM_CART', productId);
    },
    toggleCartDropdown({ commit }) {
      commit('TOGGLE_CART_DROPDOWN');
    },
  }
};
