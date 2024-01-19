<template>
  <transition name="dropdown">
    <div v-if="isDropdownVisible" class="cart-dropdown">
      <div class="cart-items">
        <div class="cart-item" v-for="item in cartItems" :key="item.id">
          <div class="item-details">
            <span class="name">{{ item.name }}</span>
            <span class="price">{{ item.quantity }} x ${{ item.price }}</span>
          </div>
          <button class="remove-item" @click="removeFromCart(item.id)">&times;</button>
        </div>
      </div>
      <router-link to="/checkout" class="checkout-button">Checkout</router-link>
    </div>
  </transition>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'CartDropdown',
  computed: {
    ...mapState({
      isDropdownVisible: state => state.cart.isCartDropdownVisible,
      cartItems: state => state.cart.items,
    }),
  },
  methods: {
    ...mapActions('cart', ['removeFromCart']),
  },
};
</script>

<style scoped>
.cart-dropdown {
  display: block;
  position: absolute;
  right: 35px; /* Adjusted for better alignment */
  top: 100%; /* Align below the Navbar */
  background-color: white;
  border: 1px solid rgba(0,0,0,.1);
  border-radius: 4px;
  width: 300px;
  padding: 20px;
  box-shadow: 0 5px 15px rgba(0,0,0,.15);
  z-index: 10;
}

.dropdown-enter-active, .dropdown-leave-active {
  transition: opacity .3s;
}

.dropdown-enter, .dropdown-leave-to {
  opacity: 0;
}

.cart-items {
  max-height: 340px;
  overflow-y: auto;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eaeaea;
}

.item-details {
  display: flex;
  flex-direction: column;
}

.name {
  font-size: 16px;
  color: #333;
}

.price {
  font-size: 14px;
  color: #555;
}

.remove-item {
  background: none;
  border: none;
  cursor: pointer;
  color: #999;
  font-size: 24px;
}

.checkout-button {
  display: block;
  width: 100%;
  padding: 10px 20px;
  background-color: #5c6bc0;
  color: white;
  text-align: center;
  border-radius: 4px;
  text-decoration: none;
  margin-top: 20px;
}
</style>
