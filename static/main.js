const {createApp} = Vue
createApp({
    delimiters: ['[[', ']]'],
    mounted() {
        let cart = JSON.parse(localStorage.getItem('cart_list') ?? '[]')
        this.cart_list = cart
    },
    data() {
        return {
            message: 'Hello World!',
            counter: 0,
            cart_list: [],
            grand_total: 0,
            shipping_fee: 1.5
        }
    },
    methods: {
        addToCart(product) {
            if (this.cart_list.length == 0) {
                product.qty = 1
                this.cart_list.push(product)
            } else {
                let dpl_pro = this.cart_list.find(item => {
                    return product.id == item.id
                })
                if (dpl_pro) {
                    dpl_pro.qty++
                } else {
                    product.qty = 1
                    this.cart_list.push(product)
                }
            }
            localStorage.setItem('cart_list', JSON.stringify(this.cart_list))

            Swal.fire({
                position: "top-end",
                icon: "success",
                title: "Product has been add to cart",
                showConfirmButton: false,
                timer: 1500
            });
        },
        removeCartItem(index) {
            Swal.fire({
                title: "Are you sure?",
                text: "You won't be able to revert this!",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes, delete it!"
            }).then((result) => {
                if (result.isConfirmed) {
                    this.cart_list.splice(index, 1)
                    localStorage.setItem('cart_list', JSON.stringify(this.cart_list))
                }
            });
        },
        calGrandTotal() {
            this.grand_total = 0
            this.cart_list.forEach(item => {
                let total = parseFloat(item.qty) * parseFloat(item.price)
                this.grand_total += total
            })
            return parseFloat(this.grand_total).toFixed(2)
        },
        addCartQty(index) {
            this.cart_list[index].qty++
            localStorage.setItem('cart_list', JSON.stringify(this.cart_list))
        },
        removeCartQty(index) {
            if (this.cart_list[index].qty > 1) {
                this.cart_list[index].qty--
                localStorage.setItem('cart_list', JSON.stringify(this.cart_list))
            } else {
                this.removeCartItem(index)
            }
        }
    }
}).mount('#app')
