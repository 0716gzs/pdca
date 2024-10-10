import { createVNode, render } from 'vue';
import Footer from './Footer.vue';

export default {
    mounted(el) {
        const footerVNode = createVNode(Footer);
        render(footerVNode, el);
    },
    unmounted(el) {
        render(null, el);
    }
};
