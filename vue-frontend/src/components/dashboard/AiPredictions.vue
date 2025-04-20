<template>
  <div class="space-y-4">
    <div
      v-for="(prediction, index) in predictions"
      :key="index"
      class="bg-white p-4 rounded-lg shadow-md border-l-4 border-blue-400"
    >
      <div class="text-lg font-semibold text-gray-800">{{ prediction.metric }}</div>
      <div class="text-xl text-blue-600">{{ prediction.value }}</div>
      <div class="text-sm text-gray-500">Confidence: {{ prediction.confidence }}%</div>
      <div class="text-xs text-gray-400">Model v1.0</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AiPredictions',
  props: {
    predictions: {
      type: Array,
      default: () => [
        { metric: 'Churn Rate', value: '12.4%', confidence: 91 },
        { metric: 'Forecasted Revenue', value: '$42,000', confidence: 88 },
      ],
    },
  },
};
</script>
