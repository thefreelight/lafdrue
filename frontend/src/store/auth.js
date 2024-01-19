// store/auth.js
export const auth = {
  namespaced: true,
  state: () => ({
    user: null,
  }),
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
  },
  actions: {
    async authenticateUser({ commit }, { email, password }) {
      try {
        // 模拟API调用
        const response = await fakeAPICall(email, password);
        commit('SET_USER', response.user);
      } catch (error) {
        console.error("Failed to authenticate user", error);
        // 在实际应用中，您可能还想在此处理错误（例如，更新状态或触发另一个mutation）
      }
    },
  },
};

// 模拟API调用函数
async function fakeAPICall(email, password) {
  // 这个函数应该调用实际的API并返回结果
  // 下面是一个示例响应
  return {
    user: { email, name: "Mock User", id: "12345" }
  };
}
