<template>
  <div>
    <component :is="currentComponent"></component>
  </div>
</template>

<script>
import PlanPage from './Plan.vue';
import DoPage from './Do.vue';
import CheckPage from './Check.vue';
import ActionPage from './Action.vue';

export default {
  props: {
    currentIndex: {
      type: String,
      default: '2'
    }
  },

  computed: {
    currentComponent() {
      switch (this.currentIndex) {
        case '1':
          return PlanPage;
        case '2':
          return DoPage;
        case '3':
          return CheckPage;
        case '4':
          return ActionPage;
        default:
          return null;
      }
    }
  }
}
</script>

<style scoped>
/* Add your styles here */
</style>
