import { createI18n } from 'vue-i18n';

const messages = {
    en: {
        message: {
            hello: 'Hello',
            home: 'Home',
            products: 'Products',
            articles: 'Articles',
            login: 'Login'
        }
    },
    zh: {
        message: {
            hello: '你好',
            home: '首页',
            products: '商店',
            articles: '文章',
            login: '登录'
        }
    }
};

const i18n = createI18n({
    legacy: false, // 使用 Composition API
    locale: 'en',
    messages
});

export default i18n;
