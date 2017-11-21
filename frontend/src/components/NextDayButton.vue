<template>
    <div class="next-day" v-show="isLoggedIn">
        <a class="next-day-button" @click="nextDay">Next day</a>
    </div>
</template>

<script>
import userController from '@/controllers/User.controller'
import cacheController from '@/controllers/Cache.controller'
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
                    this.setNewStep()
                })
        },
        increaseStep() {
            this.setStep(parseInt(this.getStep) + 1)
        },
        setNewStep() {
            cacheController.setStep(this.getStep)
        }
    }
}
</script>

<style>
    .next-day {
        position: fixed;
        right: 0;
        bottom: 0;
        margin-bottom: 16px;
        padding-left: 16px;
        height: 40px;
        width: 120px;
        background-color : #ffc400;
        border-top-left-radius: 20px;
        border-bottom-left-radius: 20px;
		box-shadow: 0 4px 2px 0 rgba(0, 0, 0, 0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }

    .next-day-button {
        font-size: 16px;
        font-weight: bold;
    }

    .next-day-button:hover {
        text-decoration: none;
    }
</style>

