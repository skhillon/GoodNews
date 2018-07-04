import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';

const styles = theme => ({
  root: {
    ...theme.mixins.gutters(),
    paddingTop: theme.spacing.unit * 2,
    paddingBottom: theme.spacing.unit * 2,
  },
});

function Footer(props) {
  const { classes } = props;

  return (
    <div>
      <Paper className={classes.root} elevation={1}>
      <center>
        <Typography variant="subheading">
          Made with ❤️ by <a href="https://github.com/skhillon">Sarthak Khillon</a>
        </Typography>
        <Typography component="p">
          Concerns? Email me <a href="mailto:sarthakkhillon24@gmail.com">here</a>.
        </Typography>
      </center>
      </Paper>
    </div>
  );
}

Footer.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Footer);