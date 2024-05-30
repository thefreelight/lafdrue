<template>
  <div class="overflow-x-auto bg-white rounded-lg shadow overflow-y-auto relative">
    <table class="border-collapse table-auto w-full whitespace-no-wrap bg-white table-striped relative">
      <thead>
        <tr class="text-left">
          <th
            v-for="header in headers"
            :key="header.text"
            class="bg-blue-100 sticky top-0 border-b border-gray-200 px-6 py-4 text-gray-600 font-bold tracking-wider uppercase text-xs"
          >
            {{ header.text }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in items"
          :key="item.id"
          class="hover:bg-gray-100"
        >
          <td
            v-for="field in headers"
            :key="field.value"
            class="px-6 py-4 border-b border-gray-200"
          >
            <slot :name="field.value" :item="item">
              {{ item[field.value] }}
            </slot>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>

const props = defineProps({
  headers: Array,
  items: Array
});
</script>

<style scoped>
/* Additional styles can be placed here if needed */
</style>
