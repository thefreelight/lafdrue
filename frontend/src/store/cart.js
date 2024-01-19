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
    },
    TOGGLE_CART_DROPDOWN(state) {
      state.isCartDropdownVisible = !state.isCartDropdownVisible;
    }
  },
  actions: {
    addToCart({ commit }, product) {
    // 提交 mutation，传入产品对象
      commit('ADD_TO_CART', product);    },
    removeFromCart({ commit }, productId) {
      commit('REMOVE_FROM_CART', productId);
    },
    toggleCartDropdown({ commit }) {
      commit('TOGGLE_CART_DROPDOWN');
    }
  }
};
