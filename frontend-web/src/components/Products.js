import react,{useEffect, useState} from 'react';
import axios from 'axios';
import {Card, CardContent, Typography, Button} from '@mui/material';

const Products = () => {
    const [products, setProducts] = useState([]);
    
    useEffect(() => {
        axios.get('http://localhost:3000/api/products')
        .then(res => setProducts(res.data))
        .catch(err => console.error(err));
    }, []);
    return (
        <div style={{ padding: '20px' }}>
            <h1>المنتجات المتاحة</h1>
            {products.map(product => (
                <Card key={product.id} style={{ margin: '10px', maxwidth: '300px' }}>
                    <CardContent>
                        <Typography variant="h5">
                            {product.name}
                        </Typography>
                        <Typography >السعر:
                            {product.price} دولار
                        </Typography>
                        <Typography >المخزون:
                            {product.stock}
                        </Typography>
                        <Button variant="contained" color="primary" style={{ marginTop: '10px' }}>
                            أضف إلى السلة
                        </Button>
                    </CardContent>
                </Card>
            ))}
        </div>
    );
};

export default Products;