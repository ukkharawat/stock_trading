<template>
    <div class="next-day" v-show="isLoggedIn" @click="nextDay">
        <a class="next-day-button">Next day</a>
    </div>
</template>

<script>
import userController from '@/controllers/User.controller'
import { mapGetters, mapActions } from 'vuex'

export default {
    computed: {
        ...mapGetters([
            'getCash',
            'getStep',
            'isLoggedIn'
        ])
    },
    methods: {
        ...mapActions([
            'setStep'
        ]),
        nextDay() {
            userController.nextDay(this.getCash, this.getStep)
                .then(response => {
                    this.increaseStep()
                })
        },
        increaseStep() {
            this.setStep(parseInt(this.getStep) + 1)
        }
    }
}
</script>
