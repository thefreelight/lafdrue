// store/index.js
import { createStore } from 'vuex';
import { auth } from './auth';
import { cart } from './cart';
import { products } from './products';

export default createStore({
  modules: {
    auth,
    cart,
    products
  }
});
